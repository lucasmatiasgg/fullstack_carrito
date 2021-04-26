from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Colum, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Colum(Integer, primary_key=True)
    firstName = Colum(String)
    lastName = Colum(String)

engine = create_engine('mysql://lgomez:password@localhost:3306/shoppingCart')

session = sessionmaker()
session.configure(bind=engine)


@app.route('/createdb')
def create_db():
    Base.metadata.create_all(engine)
    return 'ok'