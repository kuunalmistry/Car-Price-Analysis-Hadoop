import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- LOAD DATA ----------------
df = pd.read_csv("car_price_big.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")
df = df.dropna()

# ---------------- STYLE ----------------
sns.set_style("whitegrid")
blue_light = "#4ea8de"
blue_dark = "#023e8a"

# ---------------- CREATE DASHBOARD ----------------
fig = plt.figure(figsize=(16, 10))
fig.suptitle("Car Price Analysis Dashboard", fontsize=20, fontweight="bold")

# ===== 1. Average Price by Brand =====
ax1 = plt.subplot(2, 3, 1)
df.groupby("Brand")["Price"].mean().sort_values().plot(
    kind="barh", color=blue_dark, ax=ax1)
ax1.set_title("Average Price by Brand")

# ===== 2. Fuel Type Distribution =====
ax2 = plt.subplot(2, 3, 2)
df["Fuel_Type"].value_counts().plot(
    kind="pie", autopct='%1.0f%%',
    colors=[blue_dark, blue_light, "#90e0ef", "#0077b6"],
    ax=ax2)
ax2.set_ylabel("")
ax2.set_title("Fuel Type Distribution")

# ===== 3. Transmission Type =====
ax3 = plt.subplot(2, 3, 3)
df["Transmission"].value_counts().plot(
    kind="bar", color=[blue_dark, blue_light], ax=ax3)
ax3.set_title("Transmission Type")

# ===== 4. Car Condition =====
ax4 = plt.subplot(2, 3, 4)
df["Condition"].value_counts().plot(
    kind="pie", autopct='%1.0f%%',
    colors=[blue_light, blue_dark, "#90e0ef"],
    ax=ax4)
ax4.set_ylabel("")
ax4.set_title("Car Condition")

# ===== 5. Top 5 Models =====
ax5 = plt.subplot(2, 3, 5)
df["Model"].value_counts().head(5).plot(
    kind="bar", color=blue_dark, ax=ax5)
ax5.set_title("Top 5 Models")

# ===== 6. Price Distribution =====
ax6 = plt.subplot(2, 3, 6)
sns.histplot(df["Price"], bins=25,
             color=blue_light, ax=ax6)
ax6.set_title("Price Distribution")

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save as PNG
plt.savefig("dashboard.png", dpi=300)
plt.show()

print("Dashboard saved as dashboard.png")