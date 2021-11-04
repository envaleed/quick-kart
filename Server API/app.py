from flask import Flask, json, jsonify, make_response, request, redirect, url_for, abort, make_response
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import backref
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from flask_jwt import JWT, jwt_required, current_identity
import uuid


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_ENDPOINT'] = 'token'
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/supermarket'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Grocery(db.Model):
    __tablename__= 'grocery'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    grocery_type = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isle_no = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(255), nullable=False)
    tag = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Grocery %r, %r>' % (self.title, self.price)

class Users(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)
    orders = db.relationship('Orders', backref="users", lazy=True)

    def __repr__(self):
        return '<Users %r>' % self.id

    def set_password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(60), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    pickupcode = db.Column(db.String(255),nullable=False)

class GrocerySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Grocery

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

class OrdersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orders

db.create_all()
grocery_schema = GrocerySchema()
groceries_schema = GrocerySchema(many=True)
user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)

@app.errorhandler(404)
def error_404(error):
    return jsonify(error.description), 404

@app.errorhandler(500)
def error_500(error):
    return jsonify(error.description), 404

def authenticate(username, password):
    user = Users.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

def identity(payload):
    return Users.query.filter(Users.id == payload['identity']).scalar()

jwt = JWT(app,authenticate,identity)

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
        title = request.json['title']
        quantity = request.json['quantity']
        pickupcode = uuid.uuid1()
        print(current_identity)
        user_id = current_identity.id
        order = Orders(title=title, quantity=quantity,pickupcode=pickupcode, user_id=user_id)
        db.session.add(order)
        db.session.commit()
        return jsonify({"Successfully added":order.title})
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

if __name__ == '__main__':
    app.run(debug=True)



