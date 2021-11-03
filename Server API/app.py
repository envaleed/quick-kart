from flask import Flask, jsonify, make_response, request, redirect, url_for
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://supermarket:password@localhost:3307/supermarket'
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
        return '<Grocery %r>' % self.title, self.price

class Users(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return '<Users %r>' % self.username 

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

class Orders(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    pickupcode = db.Column(db.String(255),nullable=False)

class GrocerySchema(ma.ModelSchema):
    class Meta:
        model = Grocery

class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users

class OrdersSchema(ma.ModelSchema):
    class Meta:
        model = Orders

db.create_all()
grocery_schema = GrocerySchema(strict=True)
groceries_schema = GrocerySchema(many=True, strict=True)
user_schema = UsersSchema(strict=True)
users_schema = UsersSchema(many=True, strict=True)
order_schema = OrdersSchema(strict=True)
orders_schema = OrdersSchema(many=True, strict=True)

@app.route('/supermercado/api/v1.0/<username>/<password>', methods=['GET','POST'])
def login(username,password):
    user = Users.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'id':user.id, 'email':user.email})
    else:
        return error()

@app.route('/supermercado/api/v1.0/logout')
def logout():
    logout_user()
    return jsonify({'Logged Out':'Successful'})

def error():
    return jsonify({'error':'something went wrong'})

@app.route('/supermercado/api/v1.0/register/<username>/<password>/<email>', methods=['GET', 'POST'])
def register(username,password,email):
    username_ = username
    password_hash = password
    email_ = email
    if Users.query.filter_by(username = username_).first() is not None:
        return error()
    user = Users(username=username_, email=email_)
    user.set_password(password_hash)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'email': user.email})

@app.route('/supermercado/api/v1.0/search/<search>',methods=['GET'])
def get_item(search):
    search_ = str(search)
    search_ = "%"+search_+"%"
    item = Grocery.query.filter(Grocery.tag.like(search_)).all()
    item = groceries_schema.dump(item).data
    return jsonify({search:item})

@app.route('/supermercado/api/v1.0/search2/<search2>',methods=['GET'])
def get_item1(search2):
    search_ = str(search2)
    search_ = "%"+search_+"%"
    item = Grocery.query.filter(Grocery.tag.like(search_)).all()
    item = groceries_schema.dump(item).data
    return jsonify(item)

@app.route('/supermercado/api/v1.0/postorder/<code>',methods=['POST'])
def stress_exe(code):
    if not request.json:
        return error()
    id_ = request.json['id']
    title_ = request.json['title']
    quantity_ = request.json['quantity']
    pickupcode_ = code
    order = Orders(id=id_,title=title_, quantity=quantity_,pickupcode=pickupcode_)
    db.session.add(order)
    db.session.commit()
    return jsonify({"Successfully added":"yes"})

@app.route('/supermercado/api/v1.0/fetchorder/<order>',methods=['GET'])
def query_for_order(order):
    orders = Orders.query.filter_by(pickupcode=order).all()
    orders = orders_schema.dump(orders).data
    return jsonify({order:orders})

def load_user(id):
    return User.query.get(int(id))

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8008')



