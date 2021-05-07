import config

class Item(config.Base):
    __tablename__ = 'item'
    id_item = config.Column(config.Integer, primary_key=True, nullable=False)
    quantity = config.Column(config.integer)
    amount = config.Column(config.integer)
    product_id = config.Column(config.integer, config.ForeignKey('product.id_product'), nullable = False)

    dataBaseModel.product = config.relationship(dataBaseModel.product.Product)

def save(self):
    config.save_to_db(self)