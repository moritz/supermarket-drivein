from drivein.model import db, Category, Merchant
from drivein import app


with app.app_context():
    db.create_all()
    for cat in ('Lebensmittel', 'Medikamente', 'Drogerie', 'Bäcker'):
        if not Category.query.filter_by(name=cat).first():
            cat_obj = Category(name=cat)
            db.session.add(cat_obj)

    db.session.commit()
