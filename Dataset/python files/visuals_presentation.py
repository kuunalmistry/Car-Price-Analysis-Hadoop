import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("car_price_big.csv")
df.columns = df.columns.str.strip()

# Blue color palette
dark_blue = "#0B3C5D"
light_blue = "#328CC1"
soft_blue = "#A9CCE3"

plt.style.use("seaborn-v0_8-whitegrid")

# ==============================
# 1️⃣ Average Price by Brand (Bar)
# ==============================

plt.figure(figsize=(10,6))
avg_price_brand = df.groupby("Brand")["Price"].mean().sort_values(ascending=False)
avg_price_brand.plot(kind="bar", color=light_blue)
plt.title("Average Price by Brand", color=dark_blue)
plt.xlabel("Brand")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("1_avg_price_brand.png", dpi=300)
plt.close()


# ==============================
# 2️⃣ Fuel Type Distribution (Pie)
# ==============================

plt.figure(figsize=(7,7))
fuel_counts = df["Fuel Type"].value_counts()
plt.pie(fuel_counts,
        labels=fuel_counts.index,
        autopct="%1.1f%%",
        colors=[light_blue, soft_blue, dark_blue])
plt.title("Fuel Type Distribution", color=dark_blue)
plt.tight_layout()
plt.savefig("2_fuel_type_pie.png", dpi=300)
plt.close()


# ==============================
# 3️⃣ Transmission Distribution (Bar)
# ==============================

plt.figure(figsize=(8,6))
trans_counts = df["Transmission"].value_counts()
trans_counts.plot(kind="bar", color=dark_blue)
plt.title("Transmission Distribution", color=dark_blue)
plt.xlabel("Transmission")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("3_transmission_bar.png", dpi=300)
plt.close()


# ==============================
# 4️⃣ Condition Distribution (Bar)
# ==============================

plt.figure(figsize=(8,6))
condition_counts = df["Condition"].value_counts()
condition_counts.plot(kind="bar", color=light_blue)
plt.title("Car Condition Distribution", color=dark_blue)
plt.xlabel("Condition")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig("4_condition_bar.png", dpi=300)
plt.close()


# ==============================
# 5️⃣ Average Price by Year (Line - Blue)
# ==============================

plt.figure(figsize=(10,6))
year_price = df.groupby("Year")["Price"].mean()
plt.plot(year_price.index, year_price.values,
         color=dark_blue,
         linewidth=2,
         marker="o")
plt.title("Average Price by Year", color=dark_blue)
plt.xlabel("Year")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig("5_year_trend.png", dpi=300)
plt.close()


# ==============================
# 6️⃣ Top 5 Brands by Count (Bar)
# ==============================

plt.figure(figsize=(8,6))
top_brands = df["Brand"].value_counts().head(5)
top_brands.plot(kind="bar", color=soft_blue)
plt.title("Top 5 Brands by Market Presence", color=dark_blue)
plt.xlabel("Brand")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig("6_top_brands_bar.png", dpi=300)
plt.close()


# ==============================
# 7️⃣ Price Range Distribution (Pie)
# ==============================

# Create price categories
bins = [0, 20000, 40000, 60000, 80000, 100000]
labels = ["Budget", "Mid-Range", "Upper-Mid", "Premium", "Luxury"]
df["Price Range"] = pd.cut(df["Price"], bins=bins, labels=labels)

plt.figure(figsize=(7,7))
price_dist = df["Price Range"].value_counts()
plt.pie(price_dist,
        labels=price_dist.index,
        autopct="%1.1f%%",
        colors=[light_blue, soft_blue, dark_blue, "#1F618D", "#5DADE2"])
plt.title("Price Range Distribution", color=dark_blue)
plt.tight_layout()
plt.savefig("7_price_range_pie.png", dpi=300)
plt.close()

print("🔥 Blue-themed visuals generated successfully.")