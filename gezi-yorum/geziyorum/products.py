from dataclasses import dataclass
from geziyorum import db


@dataclass
class Products(db.Model):
    __tablename = "PRODUCTS"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id, product_name):
        self.id = id
        self.product_name = product_name

    @classmethod
    def get_all_products(cls):
        return cls.query.all()

    @classmethod
    def add_product(cls, number, name):
        product = cls(number, name)
        db.session.add(product)
        db.session.commit()
