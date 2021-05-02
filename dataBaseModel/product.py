import config

class Product(config.Base):
    __tablename__ = 'product'
    id_product = config.Column(config.Integer, primary_key=True, nullable=False)
    description = config.Column(config.String(100))
    price = config.Column(config.Float(50))

def save(self):
    config.save_to_db(self)