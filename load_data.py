# import pandas library
import pandas as pd

# load dataset and assign it to a variable df
df = pd.read_csv("freshmart_products.csv")
#print("\n--- First 5 Rows ---")
#print(df.head())

#dataset info
print(" Dataset Info:")
print(df.info())


#records with missing values
missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)

#drop missing values
df = df.dropna(subset=["Price", "StockQuantity"])

#check dataset after dropping missing values
print(df.info())

#save cleansed dataset
df.to_csv("products.csv", index=False)
