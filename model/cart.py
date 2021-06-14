import config
from model.historyCart import history_cart
from model.orderItem import order_item

class Cart(config.Base):
    __tablename__ = 'cart'
    cartId = config.Column(config.Integer, primary_key=True, nullable=False)
    totalAmount = config.Column(config.Float)
    userRelation = config.relationship('User', secondary=history_cart, backref=config.backref('subsUser', lazy='dynamic'))
    itemRelation = config.relationship('Item', secondary=order_item, backref=config.backref('subsItem', lazy='dynamic'))

def save(self):
    config.save_to_db(self)