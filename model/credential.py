import config
import model.user

class Credential(config.Base):
    __tablename__ = 'credential'
    credential_id = config.Column(config.Integer, primary_key=True, nullable=False)
    userName = config.Column(config.String(50))
    password = config.Column(config.String(20))
    user_id = config.Column(
        config.Integer,
        config.ForeignKey('user.user_id'),
        nullable = False
    )

    model.user = config.relationship(model.user.User)

def save(self):
    config.save_to_db(self)