from .model import db
from flask_cors import CORS
from flask import Flask, render_template, send_from_directory

def make_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///drivein'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    CORS(app)
    return app

app = make_app()
