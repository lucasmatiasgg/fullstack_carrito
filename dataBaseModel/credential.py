import config
import dataBaseModel.user

class Credential(config.Base):
    __tablename__ = 'credential'
    id = config.Column(config.Integer, primary_key=True, nullable=False)
    userName = config.Column(config.String(50))
    password = config.Column(config.String(20))
    user_id = config.Column(
        config.Integer,
        config.ForeignKey('user.id'),
        nullable = False
    )

    dataBaseModel.user = config.relationship(dataBaseModel.user.User)

def save(self):
    config.save_to_db(self)