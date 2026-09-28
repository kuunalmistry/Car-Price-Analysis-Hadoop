import matplotlib.pyplot as plt

brands = ["BMW", "Honda", "Toyota"]
prices = [2500000, 600000, 450000]

plt.figure(figsize=(8, 5))

bars = plt.bar(brands, prices)

plt.xlabel("Car Brand")
plt.ylabel("Average Price")
plt.title("Car Price Analysis (Average Price per Brand)")

plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), 
             ha='center', va='bottom')

plt.savefig("car_price_analysis.png")

plt.show()