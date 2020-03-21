from .app import app
from .model import db, Category
from flask import jsonify

@app.route('/category')
def list_categories():
    rs = Category.query
    return jsonify([c.as_json() for c in rs])
    
