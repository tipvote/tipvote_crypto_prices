from flask import Flask
from config import SQLALCHEMY_DATABASE_URI_0, SQLALCHEMY_BINDS
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI_0
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS


db = SQLAlchemy(app)
