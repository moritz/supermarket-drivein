from .app import app
from .model import db, Category, Merchant
from flask import jsonify, request

@app.route('/merchant')
def list_merchants():
    rs = Merchant.query
    return jsonify([m.as_json() for m in rs])
    
@app.route('/merchant', methods=['POST'])
def add_merchant():
    payload = request.get_json(force=True)
    mandatory = set(('name', 'address', 'category'))
    missing_attrs = [a for a in mandatory if not payload.get(a)]
    if missing_attrs:
        message = 'Missing attributes: '  + ', '.join(missing_attrs)
        return jsonify({'success': False, 'missing': missing_attrs, 'message': message})
    category = Category.query.filter_by(**payload.pop('category')).one()
    merchant = Merchant(category=category, **payload)
    db.session.add(merchant)
    db.session.commit()
    return jsonify(merchant.as_json())
    
@app.route('/merchant/<id>', methods=['DELETE'])
def delete_merchant(id):
    merchant = Merchant.query.filter_by(id=int(id)).first()
    if merchant:
        db.session.delete(merchant)
        db.session.commit()
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'No object found to delete'})
