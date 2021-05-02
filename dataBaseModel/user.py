import config
from sqlalchemy import Column, Integer, String

class User(config.Base):
    __tablename__ = 'user'
    id = config.Column(config.Integer, primary_key=True)
    firstName = config.Column(config.String(50))
    lastName = config.Column(config.String(50))