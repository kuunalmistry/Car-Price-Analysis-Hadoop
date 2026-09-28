import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle

# ---------------- LOAD DATA ----------------
df = pd.read_csv("car_price_big.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")
df = df.dropna()

# ---------------- STYLE ----------------
sns.set_style("darkgrid")

dark_bg = "#0E1117"
panel_bg = "#161B22"
blue_primary = "#1f77b4"
blue_light = "#4ea8de"
accent = "#00B4D8"
text_color = "white"
green = "#2ecc71"
red = "#e74c3c"

# ---------------- KPI CALCULATIONS ----------------
total_cars = len(df)
avg_price = df["Price"].mean()
brand_avg = df.groupby("Brand")["Price"].mean()
premium_brand = brand_avg.idxmax()
budget_brand = brand_avg.idxmin()
premium_price = brand_avg.max()
budget_price = brand_avg.min()

most_common_fuel = df["Fuel_Type"].value_counts()
fuel_name = most_common_fuel.idxmax()
fuel_percent = round((most_common_fuel.max()/total_cars)*100,1)

# Performance indicators
premium_vs_avg = premium_price - avg_price
indicator_arrow = "↑" if premium_vs_avg > 0 else "↓"
indicator_color = green if premium_vs_avg > 0 else red

# ---------------- FIGURE ----------------
fig = plt.figure(figsize=(18, 10))
fig.patch.set_facecolor(dark_bg)

# Subtle gradient
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
ax_grad = fig.add_axes([0, 0, 1, 1])
ax_grad.imshow(gradient, aspect='auto', cmap=plt.get_cmap("Blues"), alpha=0.06)
ax_grad.axis("off")

# ---------------- HEADER ----------------
plt.figtext(0.5, 0.95, "Car Price Executive Performance Dashboard",
            ha="center", fontsize=24, fontweight="bold", color=text_color)

plt.figtext(0.5, 0.92, "Market Leadership | Brand Strength | Strategic Insights",
            ha="center", fontsize=11, color="#BBBBBB")

# ---------------- KPI CARD FUNCTION ----------------
def kpi_card(x, title, value):
    ax = fig.add_axes([x, 0.82, 0.25, 0.08])
    ax.set_facecolor(panel_bg)
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 1, 1,
                           facecolor=panel_bg,
                           edgecolor=accent,
                           linewidth=1.5))
    ax.text(0.05, 0.60, title, fontsize=11, color="#AAAAAA")
    ax.text(0.05, 0.20, value,
            fontsize=18, fontweight="bold",
            color=text_color)

kpi_card(0.05, "Total Vehicles", f"{total_cars:,}")
kpi_card(0.37, "Market Average Price", f"${round(avg_price,2):,}")
kpi_card(0.69, "Premium Brand Leader", premium_brand)

# ---------------- PANEL FUNCTION ----------------
def panel(x, y, w, h, title):
    ax = fig.add_axes([x, y, w, h])
    ax.set_facecolor(panel_bg)
    for spine in ax.spines.values():
        spine.set_edgecolor("#2A2F3A")
        spine.set_linewidth(1.2)
    ax.set_title(title, fontsize=12, color=text_color, pad=10)
    ax.tick_params(colors="white")
    return ax

# ---------------- CHARTS ----------------

# Avg Price by Brand
ax1 = panel(0.05, 0.48, 0.27, 0.28, "Average Price by Brand")
brand_avg.sort_values().plot(
    kind="barh", color=blue_primary, ax=ax1)

# Fuel Distribution
ax2 = panel(0.37, 0.48, 0.27, 0.28, "Fuel Type Distribution")
df["Fuel_Type"].value_counts().plot(
    kind="pie", autopct='%1.0f%%',
    colors=[blue_primary, blue_light, "#0077b6", "#00B4D8"],
    textprops={'color':"white"},
    ax=ax2)
ax2.set_ylabel("")

# Transmission
ax3 = panel(0.69, 0.48, 0.27, 0.28, "Transmission Type")
df["Transmission"].value_counts().plot(
    kind="bar", color=[blue_primary, blue_light], ax=ax3)

# Price Distribution
ax4 = panel(0.05, 0.10, 0.27, 0.28, "Price Distribution")
sns.histplot(df["Price"], bins=25,
             color=blue_light, ax=ax4)

# Top Models
ax5 = panel(0.37, 0.10, 0.27, 0.28, "Top 5 Models")
df["Model"].value_counts().head(5).plot(
    kind="bar", color=blue_primary, ax=ax5)

# ---------------- EXECUTIVE INSIGHTS PANEL ----------------
insight_ax = fig.add_axes([0.69, 0.10, 0.27, 0.28])
insight_ax.set_facecolor(panel_bg)
insight_ax.axis("off")
insight_ax.add_patch(Rectangle((0, 0), 1, 1,
                               facecolor=panel_bg,
                               edgecolor=accent,
                               linewidth=1.5))

insight_text = f"""
EXECUTIVE PERFORMANCE SUMMARY

{indicator_arrow} {premium_brand} leads the market
   by ${round(premium_vs_avg,2):,} above average.

↓ {budget_brand} operates in the
   lowest price segment.

⚡ {fuel_name} dominates fuel market
   with {fuel_percent}% share.

📊 Total dataset covers {total_cars:,}
   vehicles across multiple brands.
"""

insight_ax.text(0.05, 0.90, insight_text,
                fontsize=11, color=text_color,
                verticalalignment="top")

# ---------------- SAVE ----------------
plt.savefig("executive_pro_dashboard.png", dpi=300)
plt.show()

print("Executive Performance Dashboard saved as executive_pro_dashboard.png")