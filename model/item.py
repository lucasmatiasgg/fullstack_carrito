import config
import model.product

class Item(config.Base):
    __tablename__ = 'item'
    item_id = config.Column(config.Integer, primary_key=True, nullable=False)
    quantity = config.Column(config.Integer)
    amount = config.Column(config.Integer)
    productId = config.Column(config.Integer, config.ForeignKey('product.productId'), nullable = False)

    model.product = config.relationship(model.product.Product)

def save(self):
    config.save_to_db(self)