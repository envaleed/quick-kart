from flask import Flask, json, jsonify, make_response, request, redirect, url_for, abort, make_response
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt


app = Flask(__name__)
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

    def __repr__(self):
        return '<Users %r>' % self.username 

    def set_password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Orders(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
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

@app.route('/api/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        user = Users.query.filter_by(username=username).first()
        if user and user.check_password(password):
            user = user_schema.dump(user)
            return jsonify(user)
    return abort(500,"Invalid username or password")

@app.route('/api/logout')
def logout():
    logout_user()
    return jsonify({'Logged Out':'Successful'})


@app.route('/api/registration/', methods=['POST'])
def registration():
    if request.method == "POST":
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        if Users.query.filter_by(username = username).first():
            abort(500,"This username is already taken, please enter a different one")
        if Users.query.filter_by(email = email).first():
            abort(500,"This email is already registered, please enter a different one")
        user = Users(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'id': user.id, 'email': user.email})
    return abort(500)

@app.route('/api/search/<search>',methods=['GET'])
def get_item(search):
    search_ = str(search)
    search_ = "%"+search_+"%"
    item = Grocery.query.filter(Grocery.tag.like(search_)).all()
    item = groceries_schema.dump(item)
    return jsonify({search:item})

@app.route('/api/search2/<search2>',methods=['GET'])
def get_item1(search2):
    search_ = str(search2)
    search_ = "%"+search_+"%"
    item = Grocery.query.filter(Grocery.tag.like(search_)).all()
    item = groceries_schema.dump(item).data
    return jsonify(item)

@app.route('/api/postorder/<code>',methods=['POST'])
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

@app.route('/api/fetchorder/<order>',methods=['GET'])
def query_for_order(order):
    orders = Orders.query.filter_by(pickupcode=order).all()
    orders = orders_schema.dump(orders).data
    return jsonify({order:orders})

def load_user(id):
    return User.query.get(int(id))

    
if __name__ == '__main__':
    app.run(debug=True)



