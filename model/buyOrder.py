import config
import model.user

class BuyOrder(config.Base):
    __tablename__ = 'buy_order'
    id = config.Column(config.Integer, primary_key=True, nullable=False)
    user_id = config.Column(config.Integer, config.ForeignKey('user.user_id'), nullable = False)

    # dataBaseModel.user = config.relationship(dataBaseModel.user.User)

def save(self):
    config.save_to_db(self)