from flask import Flask, request , Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'