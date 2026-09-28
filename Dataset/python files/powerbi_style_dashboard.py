import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- LOAD DATA ----------------
df = pd.read_csv("car_price_big.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")
df = df.dropna()

# ---------------- STYLE ----------------
sns.set_style("white")
blue_dark = "#1f4e79"
blue_light = "#4ea8de"
bg_color = "#f4f6f9"

# ---------------- KPIs ----------------
total_cars = len(df)
avg_price = round(df["Price"].mean(), 2)
most_expensive_brand = df.groupby("Brand")["Price"].mean().idxmax()

# ---------------- FIGURE ----------------
fig = plt.figure(figsize=(18, 10))
fig.patch.set_facecolor(bg_color)

# ---------------- HEADER ----------------
plt.figtext(0.5, 0.96, "Car Price Analysis Dashboard",
            ha="center", fontsize=22, fontweight="bold", color=blue_dark)

# ---------------- KPI CARDS ----------------
def kpi_card(x, title, value):
    plt.gcf().text(x, 0.88, title,
                   fontsize=12, color="gray", ha="left")
    plt.gcf().text(x, 0.84, value,
                   fontsize=18, fontweight="bold",
                   color=blue_dark, ha="left")

kpi_card(0.08, "Total Cars", f"{total_cars:,}")
kpi_card(0.38, "Average Price", f"${avg_price:,}")
kpi_card(0.68, "Premium Brand", most_expensive_brand)

# ---------------- GRID LAYOUT ----------------

# Avg Price by Brand
ax1 = plt.axes([0.05, 0.50, 0.27, 0.28])
df.groupby("Brand")["Price"].mean().sort_values().plot(
    kind="barh", color=blue_dark, ax=ax1)
ax1.set_title("Average Price by Brand", fontsize=12)

# Fuel Distribution
ax2 = plt.axes([0.37, 0.50, 0.27, 0.28])
df["Fuel_Type"].value_counts().plot(
    kind="pie", autopct='%1.0f%%',
    colors=[blue_dark, blue_light, "#90e0ef", "#0077b6"],
    ax=ax2)
ax2.set_ylabel("")
ax2.set_title("Fuel Type Distribution")

# Transmission
ax3 = plt.axes([0.69, 0.50, 0.27, 0.28])
df["Transmission"].value_counts().plot(
    kind="bar", color=[blue_dark, blue_light], ax=ax3)
ax3.set_title("Transmission Type")

# Condition
ax4 = plt.axes([0.05, 0.10, 0.27, 0.28])
df["Condition"].value_counts().plot(
    kind="pie", autopct='%1.0f%%',
    colors=[blue_light, blue_dark, "#90e0ef"],
    ax=ax4)
ax4.set_ylabel("")
ax4.set_title("Car Condition")

# Top Models
ax5 = plt.axes([0.37, 0.10, 0.27, 0.28])
df["Model"].value_counts().head(5).plot(
    kind="bar", color=blue_dark, ax=ax5)
ax5.set_title("Top 5 Models")

# Price Distribution
ax6 = plt.axes([0.69, 0.10, 0.27, 0.28])
sns.histplot(df["Price"], bins=25,
             color=blue_light, ax=ax6)
ax6.set_title("Price Distribution")

# ---------------- SAVE ----------------
plt.savefig("powerbi_dashboard.png", dpi=300)
plt.show()

print("Power BI style dashboard saved as powerbi_dashboard.png")