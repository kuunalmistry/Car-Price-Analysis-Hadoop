import pandas as pd

# Load original dataset
df = pd.read_csv("car_price_prediction_.csv")

# Multiply dataset (change 100 to increase size more)
large_df = pd.concat([df]*1000, ignore_index=True)

# Save expanded dataset
large_df.to_csv("car_price_big.csv", index=False)

print("Done! New dataset created.")