import config
import model.product

class Item(config.Base):
    __tablename__ = 'item'
    id_item = config.Column(config.Integer, primary_key=True, nullable=False)
    quantity = config.Column(config.Integer)
    amount = config.Column(config.Integer)
    product_id = config.Column(config.Integer, config.ForeignKey('product.id_product'), nullable = False)

    model.product = config.relationship(model.product.Product)

def save(self):
    config.save_to_db(self)