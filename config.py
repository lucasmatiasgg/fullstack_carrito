from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine

DEBUG = False

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://lgomez:password@localhost:3306')

session = sessionmaker()
session.configure(bind=engine)
session  = session()

def create_db():
    # Crea la BD si no existe
    
    engine.execute("CREATE DATABASE IF NOT EXISTS {0}".format('shoppingCart'))
    engine.execute("USE {0}".format('shoppingCart'))

def init_db():
    # Crea BD despues de levantar.
    create_db()

    # Crea todas las tablas en la BD, si ya exiten no las crea.
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    print("---DB inicializada---")

def drop_db():
    # Drop DB solo si existe
    engine.execute("DROP DATABASE IF EXISTS {0}".format('shoppingCart'))

    print("---Dropped DB!---")

def save_to_db(record):
    try:
        session.add(record)
        session.commit()
    except Exception as e:
        print (e)
