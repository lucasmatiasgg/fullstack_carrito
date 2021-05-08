import config

class User(config.Base):
    __tablename__ = 'user'
    id = config.Column(config.Integer, primary_key=True, nullable=False)
    firstName = config.Column(config.String(50))
    lastName = config.Column(config.String(50))


def save(self):
    config.save_to_db(self)