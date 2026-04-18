import pandas as pd
from domain.purchases.PurchaseOrderRepository import PurchaseOrderRepository

pd.set_option('display.width', 600)
pd.set_option('display.max_columns', 20)

# Load the data
df = PurchaseOrderRepository.load_purchase_order_csv()

# 1. Shape - how many rows and columns
print("Shape:", df.shape)

# 2. Column names
print("\nColumns:", df.columns.tolist())

# 3. Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# 4. Look at the Item Name column specifically
print("\nSample Item Names:\n", df['Item Name'].head(20))