import config

class Cart(config.Base):
    __tablename__ = 'cart'
    id = config.Column(config.Integer, primary_key=True, nullable=False)
    date = config.Column(config.Date)
    totalAmount = config.Column(config.Float)

def save(self):
    config.save_to_db(self)