# sales_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\RIZIKI\Desktop\sales_data.csv")

# Basic summary
print("Sales Summary:")
print(df.groupby("Product")[["Units Sold", "Revenue"]].sum())

# Revenue over time
daily_revenue = df.groupby("Date")["Revenue"].sum()

# Plot revenue trend
plt.figure(figsize=(8, 4))
daily_revenue.plot(kind="line", marker="o", title="Daily Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("daily_revenue.png")
plt.show()
