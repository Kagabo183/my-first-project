
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_excel(r"C:\Users\RIZIKI\Downloads\Find data from 1994.xlsx", sheet_name="Data")

# Extract years and indicator columns
years = df["Indicators in Rwanda"]
indicators = df.columns[1:] 

# Function to create a trendline chart for each indicator
def create_trendline_chart(years, values, indicator_name):
    plt.figure(figsize=(10, 6))
    
    # Plot actual data points
    plt.plot(years, values, label="Actual", marker='o', color='b')
    
    # Calculate and plot the trendline 
    z = np.polyfit(years, values, 1) 
    p = np.poly1d(z)
    plt.plot(years, p(years), label="Trendline", linestyle="--", color="r")
    
    # Add labels and title
    plt.title(f"{indicator_name} with Trendline")
    plt.xlabel("Year")
    plt.ylabel(indicator_name)
    plt.legend()

    # Show all year ticks on x-axis
    plt.xticks(years, rotation=45)  
    
    # Save the plot as a PNG file
    save_path = r"C:\Users\RIZIKI\Downloads\{}_trend.png".format(indicator_name)
    plt.savefig(save_path)  # Save to the specified path
    
    # Show the plot inline in Jupyter
    plt.show()

# Generate trendline charts for each indicator
for indicator in indicators:
    values = df[indicator]  # Get values for each indicator
    create_trendline_chart(years, values, indicator)

