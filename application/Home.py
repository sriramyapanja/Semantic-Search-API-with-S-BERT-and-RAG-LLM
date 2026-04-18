from flask import Flask, Response
from flasgger import Swagger
from domain.purchases.PurchaseOrderRepository import PurchaseOrderRepository

app = Flask(__name__)
Swagger(app)


class SemanticSearchTestApi:

    @staticmethod
    @app.route('/')
    def welcome():
        return 'Welcome.'

    @staticmethod
    def load_dataframe():
        purchaseOrderRepository = PurchaseOrderRepository()
        df_purchase_order = purchaseOrderRepository.load_purchase_order_parquet()
        return df_purchase_order

    @staticmethod
    @app.route('/purchases', methods=['GET'])
    def get_purchases_orders():
        """Get a purchase list
        ---
        tags:
          - Get all purchases
        responses:
          200:
            description: Success to get a purchase list.
          500:
            description: Failure to get a purchase list.
        """
        df_purchase_order = SemanticSearchTestApi.load_dataframe()
        # print(df_purchase_order.head(10))
        return Response(
            df_purchase_order.head(10).to_json(orient="records"),
            mimetype='application/json'
        ), 200


if __name__ == '__main__':
    app.run(debug=True)