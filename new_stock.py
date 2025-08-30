# import pandas and numpy library
import pandas as pd

# load dataset and assign it to a variable df
df = pd.read_csv("products.csv")

#create stockvalue column
df["StockValue"] = df["Price"] * df["StockQuantity"]
print(df.head())


#calculate the average price by category
avg_price = df.groupby("Category")["Price"].mean().reset_index()
avg_price.rename(columns={"Price": "AveragePrice"}, inplace=True)

# Round AveragePrice to 2 decimal places
avg_price["AveragePrice"] = avg_price["AveragePrice"].round(2)

#print average price
print("\n--- Average Price for each Category ---\n")
print(avg_price)


#Calculate total stock quantity by category
total_stock = df.groupby("Category")["StockQuantity"].sum().reset_index()
total_stock.rename(columns={"StockQuantity": "TotalStock"}, inplace=True)

print("\n--- Total StockQuantity for each Category ---\n")
print(total_stock)