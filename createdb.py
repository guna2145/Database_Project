import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLAlchemy['SQLALCHEMY_DATABASE_URI'] = '/home/logan/Documents/Database_Project'


SQLAlchemy(app)
app.config(SQLAlchemy)

