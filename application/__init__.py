from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+os.getenv('MY_SQL_USER')+":"+os.getenv('MY_SQL_PASS')+"@34.89.113.56/dbase"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = os.getenv('SECRET_PASS')

from application import routes


