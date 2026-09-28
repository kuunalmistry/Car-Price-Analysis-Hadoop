import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle

# ---------------- LOAD DATA ----------------
df = pd.read_csv("car_price_big.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")
df = df.dropna()

# ---------------- STYLE ----------------
sns.set_style("white")

blue_dark = "#0A2540"
blue_primary = "#1f77b4"
blue_light = "#4ea8de"
bg_color = "#eef2f7"
panel_bg = "white"

# ---------------- KPI VALUES ----------------
total_cars = len(df)
avg_price = round(df["Price"].mean(), 2)
premium_brand = df.groupby("Brand")["Price"].mean().idxmax()

# ---------------- FIGURE ----------------
fig = plt.figure(figsize=(18, 10))
fig.patch.set_facecolor(bg_color)

# ---------------- HEADER ----------------
plt.figtext(0.5, 0.96, "Car Price Executive Dashboard",
            ha="center", fontsize=24, fontweight="bold", color=blue_dark)

plt.figtext(0.5, 0.93, "Market Overview & Pricing Insights",
            ha="center", fontsize=12, color="gray")

# ---------------- KPI CARDS ----------------
def kpi_box(x, title, value):
    ax = fig.add_axes([x, 0.82, 0.25, 0.08])
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 1, 1,
                           facecolor=panel_bg,
                           edgecolor="#d9dee7",
                           linewidth=1.5))
    ax.text(0.05, 0.60, title, fontsize=11, color="gray")
    ax.text(0.05, 0.20, value,
            fontsize=18, fontweight="bold",
            color=blue_dark)

kpi_box(0.05, "Total Vehicles", f"{total_cars:,}")
kpi_box(0.37, "Average Price", f"${avg_price:,}")
kpi_box(0.69, "Premium Brand", premium_brand)

# ---------------- PANEL FUNCTION ----------------
def panel(x, y, w, h, title):
    ax = fig.add_axes([x, y, w, h])
    ax.set_facecolor(panel_bg)
    for spine in ax.spines.values():
        spine.set_edgecolor("#d9dee7")
        spine.set_linewidth(1.5)
    ax.set_title(title, fontsize=12, pad=10)
    return ax

# ---------------- CHART PANELS ----------------

# 1 Avg Price by Brand
ax1 = panel(0.05, 0.48, 0.27, 0.28, "Average Price by Brand")
df.groupby("Brand")["Price"].mean().sort_values().plot(
    kind="barh", color=blue_primary, ax=ax1)

# 2 Fuel Distribution
ax2 = panel(0.37, 0.48, 0.27, 0.28, "Fuel Type Distribution")
df["Fuel_Type"].value_counts().plot(
    kind="pie", autopct='%1.0f%%',
    colors=[blue_primary, blue_light, "#90e0ef", "#0077b6"],
    ax=ax2)
ax2.set_ylabel("")

# 3 Transmission
ax3 = panel(0.69, 0.48, 0.27, 0.28, "Transmission Type")
df["Transmission"].value_counts().plot(
    kind="bar", color=[blue_primary, blue_light], ax=ax3)

# 4 Condition
ax4 = panel(0.05, 0.10, 0.27, 0.28, "Vehicle Condition")
df["Condition"].value_counts().plot(
    kind="pie", autopct='%1.0f%%',
    colors=[blue_light, blue_primary, "#90e0ef"],
    ax=ax4)
ax4.set_ylabel("")

# 5 Top Models
ax5 = panel(0.37, 0.10, 0.27, 0.28, "Top 5 Models")
df["Model"].value_counts().head(5).plot(
    kind="bar", color=blue_primary, ax=ax5)

# 6 Price Distribution
ax6 = panel(0.69, 0.10, 0.27, 0.28, "Price Distribution")
sns.histplot(df["Price"], bins=25,
             color=blue_light, ax=ax6)

# ---------------- SAVE ----------------
plt.savefig("executive_dashboard.png", dpi=300)
plt.show()

print("Executive dashboard saved as executive_dashboard.png")