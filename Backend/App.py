from flask import Flask, jsonify, request
from flask import redirect, url_for
from flask_cors import CORS
import flask_sqlalchemy as sqlalchemy
import datetime
import flask

############################################################################
##################### CONNECT TO THE DATABASE ##############################

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///App.db'

db = sqlalchemy.SQLAlchemy(app)

############################################################################
############################# Data Tables ##################################

class Customer(db.model):
    oder_id = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    street = db.Column(db.String(100), nullable = False)
    apprtment_number = db.Column(db.String(50), nullable = True)
    zipcode = db.Column(db.String(50), nullable = False)
    city = db.Column(db.String(50), nullable = False)
    state = db.Column(db.String(50), nullable = False)
    
class Order(db.model):
    oder_id = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    item_key = db.Column(db.Integer, nullable = False)
    promotion_code = db.Column(db.String(50),nullable = True)
    small = db.Column(db.Integer, nullable = True)
    medium = db.Column(db.Integer, nullable = True)
    large = db.Column(db.Integer, nullable = True)
    x_large = db.Column(db.Integer, nullable = True)
    # TODO add aditional sizes
    
class Stock(db.model):
    item_key = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    small = db.Column(db.Integer, nullable = True)
    medium = db.Column(db.Integer, nullable = True)
    large = db.Column(db.Integer, nullable = True)
    x_large = db.Column(db.Integer, nullable = True)
    # TODO add aditional sizes
      
class Item(db.model):
    item_key = db.Column(db.Integer, nullable = False, primary_key=True, unique = True)
    item_number = db.Column(db.Integer, nullable = False)
    item_vendor = db.Column(db.String(50), nullable = False)
    item_description = db.Column(db.String(200), nullable = True)
    # TODO add photo to the table
    
    
    
         
        
    
    
        
    
    




