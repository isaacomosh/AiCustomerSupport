from datetime import datetime
from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(160), nullable=False, unique=True)
    description = db.Column(db.Text, default="")
    price = db.Column(db.Float, nullable=False)
    compare_at_price = db.Column(db.Float, nullable=True)
    image = db.Column(db.String(255), default="")
    stock = db.Column(db.Integer, default=25)
    is_featured = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Float, default=4.5)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def in_stock(self):
        return self.stock > 0

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "price": self.price,
            "image": self.image,
            "category": self.category.name if self.category else None,
            "in_stock": self.in_stock(),
        }

    def __repr__(self):
        return f"<Product {self.name}>"
