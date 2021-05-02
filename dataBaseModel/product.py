import config
from sqlalchemy import Column, Integer, String, Float

class Product(config.Base):
    __tablename__ = 'product'
    id_product = config.Column(config.Integer, primary_key=True)
    description = config.Column(config.String(100))
    price = config.Column(config.Float(50))