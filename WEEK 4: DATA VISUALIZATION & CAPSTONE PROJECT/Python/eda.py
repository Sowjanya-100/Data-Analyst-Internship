
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("cleaned_data.csv", parse_dates=["Date"])

# 1. Overall business performance
print("\n--- Overall Business Performance ---")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Units Sold:", round(df["Units Sold"].sum(), 2))
print("Average Sales:", round(df["Sales"].mean(), 2))
print("Average Profit:", round(df["Profit"].mean(), 2))

# 2. Sales and profit by country
print("\n--- Performance by Country ---")
country_summary = df.groupby("Country").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values("Total_Sales", ascending=False)

print(country_summary)

# 3. Sales and profit by product
print("\n--- Performance by Product ---")
product_summary = df.groupby("Product").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values("Total_Sales", ascending=False)

print(product_summary)

# 4. Performance by customer segment
print("\n--- Performance by Segment ---")
segment_summary = df.groupby("Segment").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values("Total_Sales", ascending=False)

print(segment_summary)

# 5. Yearly performance
print("\n--- Yearly Performance ---")
year_summary = df.groupby("Year").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_index()

print(year_summary)

# 6. Monthly performance
print("\n--- Monthly Performance ---")
monthly_summary = df.groupby(
    ["Year", "Month Number", "Month Name"]
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index().sort_values(["Year", "Month Number"])

print(monthly_summary.to_string(index=False))

# 7. Discount band analysis
print("\n--- Performance by Discount Band ---")
discount_summary = df.groupby("Discount Band").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Discounts=("Discounts", "sum")
).sort_values("Total_Sales", ascending=False)

print(discount_summary)

# 8. Save analysis summaries
country_summary.to_csv("country_summary.csv")
product_summary.to_csv("product_summary.csv")
segment_summary.to_csv("segment_summary.csv")
year_summary.to_csv("year_summary.csv")
monthly_summary.to_csv("monthly_summary.csv")
discount_summary.to_csv("discount_summary.csv")

print("\nAnalysis summaries saved successfully!")
