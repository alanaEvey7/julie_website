from flask import Flask, jsonify, request
from flask import redirect, url_for
from flask_cors import CORS
import flask_sqlalchemy as sqlalchemy
import datetime
import flask
from passlib.hash import sha256_crypt

############################################################################
##################### CONNECT TO THE DATABASE ##############################

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///App.db'
app.config['SQLALCHEMY_BINDS'] = {
	'login': 'sqlite:///Login.db'
}
db = sqlalchemy.SQLAlchemy(app)

############################################################################
############################# Data Tables ##################################

class Customer(db.Model):
    oder_id = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    street = db.Column(db.String(100), nullable = False)
    apprtment_number = db.Column(db.String(50), nullable = True)
    zipcode = db.Column(db.String(50), nullable = False)
    city = db.Column(db.String(50), nullable = False)
    state = db.Column(db.String(50), nullable = False)
    # TODO Ensure this data is properly encrypted
    
class Order(db.Model):
    oder_id = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    item_key = db.Column(db.Integer, nullable = False)
    promotion_code = db.Column(db.String(50),nullable = True)
    notes = db.Column(db.String(200),nullable = True)
    small = db.Column(db.Integer, nullable = True)
    medium = db.Column(db.Integer, nullable = True)
    large = db.Column(db.Integer, nullable = True)
    x_large = db.Column(db.Integer, nullable = True)
    # TODO add aditional sizes
    
class Stock(db.Model):
    item_key = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    small = db.Column(db.Integer, nullable = True)
    medium = db.Column(db.Integer, nullable = True)
    large = db.Column(db.Integer, nullable = True)
    x_large = db.Column(db.Integer, nullable = True)
    # TODO add aditional sizes
      
class Item(db.Model):
    item_key = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    item_number = db.Column(db.Integer, nullable = False)
    item_vendor = db.Column(db.String(50), nullable = False)
    item_description = db.Column(db.String(200), nullable = True)
    # TODO add photo to the table
    
class Login(db.Model):
    __bind_key__ = 'login'
    username = db.Column(db.String(50),nullable = False, primary_key=True,unique=True)
    password = db.Column(db.String(300), nullable = False)
    is_admin = db.Column(db.Boolean, nullable = False) 
    admin_code = db.Column(db.String(300), nullable = False)
    # TODO Ensure this data is properly encrypted
        
    
    
        
    
    




