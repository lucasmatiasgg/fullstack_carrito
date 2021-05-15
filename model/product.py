import config
# from model.products_to_dict import ProductsToDict

class ProductsToDict():
  def products_to_dict(self):
    return { col.name: getattr(self, col.name) for col in self.__table__.columns }

class Product(config.Base, ProductsToDict):
    __tablename__ = 'product'
    product_id = config.Column(config.Integer, primary_key=True, nullable=False)
    name = config.Column(config.String(50))
    description = config.Column(config.String(100))
    price = config.Column(config.Float(50))

def save(self):
    config.save_to_db(self)