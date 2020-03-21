from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)

    def as_json(self):
        return {'id': self.id, 'name': self.name}

class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    category_id = db.Column(db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category')

    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    url_website = db.Column(db.String)
    url_online_shopping = db.Column(db.String)

    out_of_stock = db.Column(db.String)
    payment_methods = db.Column(db.String)

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'category': self.category.as_json(),
            'latitude': self.latitude,
            'longitude': self.longitude,
            'url_website': self.url_website,
            'url_online_shopping': self.url_online_shopping,
            'out_of_stock': self.out_of_stock,
            'payment_methods': self.payment_methods,
        }
