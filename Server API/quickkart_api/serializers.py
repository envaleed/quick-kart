from quickkart_api import app
from quickkart_api.models import Grocery, Users, Orders
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

class GrocerySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Grocery

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

class OrdersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orders

grocery_schema = GrocerySchema()
groceries_schema = GrocerySchema(many=True)
user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)