from re import I
from flask import jsonify, request, abort
from flask_bcrypt import Bcrypt
from flask_jwt import jwt_required, current_identity
import uuid
from quickkart_api.models import Users, Grocery, Orders, bcrypt, db
from quickkart_api.serializers import groceries_schema, orders_schema

from quickkart_api import app

@app.route('/api/registration/', methods=['POST'])
def registration():
    if request.method == "POST" and request.json:
        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]
        if not Users.query.filter_by(username=username).first() and not Users.query.filter_by(email=email).first():
            password = bcrypt.generate_password_hash(password)
            user = Users(username=username,password_hash=password,email=email)
            db.session.add(user)
            db.session.commit()
            return jsonify({"You have successfully registered":user.username})
        return abort(500,"The username or email is already in use")
    return abort(500)


@app.route('/api/search/',methods=['POST'])
@jwt_required()
def search_item():
    if request.method == "POST" and request.json:
        keyword = request.json['keyword']
        keyword = "%"+keyword+"%"
        item = Grocery.query.filter(Grocery.tag.like(keyword)).all()
        item = groceries_schema.dump(item)
        return jsonify(item)


@app.route('/api/postorder/',methods=['POST'])
@jwt_required()
def post_order():
    if request.method == "POST" and request.json:
        orders_array = []
        for orders in request.json:
            title = orders['title']
            quantity = orders['quantity']
            pickupcode = uuid.uuid1()
            user_id = current_identity.id
            order = Orders(title=title, quantity=quantity,pickupcode=pickupcode, user_id=user_id)
            orders_array.append(order)
        db.session.add_all(orders_array)
        db.session.commit()
        orders_array = orders_schema.dump(orders_array)
        return jsonify({"orders":orders_array})
    return abort(500)

@app.route('/api/findorders/<id>/',methods=['GET'])
def find_orders(id):
    orders = Orders.query.filter_by(user_id=id).all()
    orders = orders_schema.dump(orders)
    return jsonify(orders)

@app.route('/api/findorder/<id>/<title>/',methods=['GET'])
def find_order(id,title):
    order = Orders.query.filter_by(user_id=id,title=title)
    order = orders_schema.dump(order)
    return jsonify(order)