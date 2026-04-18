import pandas as pd
from domain.purchases.PurchaseOrderRepository import PurchaseOrderRepository

pd.set_option('display.width', 600)
pd.set_option('display.max_columns', 20)


class PurchaseOrderStatistics:
    """Statistics Class"""

    def __init__(self):
        self.purchaseOrderRepository = PurchaseOrderRepository()
        self.df_purchase_order = self.purchaseOrderRepository.load_purchase_order_csv()

    def view_statistics(self):
        """View Statistics"""
        try:
            print("--- > Dataset Purchase Order:")
            print(self.df_purchase_order)

            print("\n--- > Total Rows Dataset Purchase Order:")
            print(self.df_purchase_order.shape[0])

            print("\n--- > Columns Dataset Purchase Order:")
            print(self.df_purchase_order.columns)

            print("\n--- > Total Columns Dataset Purchase Order:")
            print(len(self.df_purchase_order.columns))

            print("\n--- > Describing the Dataset Purchase Order:")
            print(self.df_purchase_order.describe())

            print("\n--- > Unique values from column Department Name (Dataset Purchase Order):")
            print(self.df_purchase_order['Department Name'].unique())

            print("\n--- > Size Records - Unique values from column Department Name (Dataset Purchase Order)")
            print(len(self.df_purchase_order['Department Name'].unique()))

            print("\n--- > Unique values from column Supplier Name (Dataset Purchase Order):")
            print(self.df_purchase_order['Supplier Name'].unique())

            print("\n--- > Size Records - Unique values from column Supplier Name (Dataset Purchase Order):")
            print(len(self.df_purchase_order['Supplier Name'].unique()))

        except Exception as e:
            print("Error to show statistics: " + e.__str__())


# Run the class
purchaseOrderStatistics = PurchaseOrderStatistics()
purchaseOrderStatistics.view_statistics()