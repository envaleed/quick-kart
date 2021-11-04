from  quickkart_api import app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

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
    title = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    pickupcode = db.Column(db.String(255),nullable=False)