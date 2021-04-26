from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

app = Flask (__name__)
app.debug = True


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(50))

engine = create_engine('mysql+mysqlconnector://lgomez:password@localhost:3306/shoppingCart')

session = sessionmaker()
session.configure(bind=engine)


@app.route('/createdb')
def create_db():
    Base.metadata.create_all(engine)
    return 'ok'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
