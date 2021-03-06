from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Table, LargeBinary
from sqlalchemy import create_engine

DEBUG = False

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://lgomez:password@localhost:3306')
# engine = create_engine('mysql+mysqlconnector://admin:password@shoppingcart.cnppf1iajcbc.us-east-1.rds.amazonaws.com:3306')

session = sessionmaker()
session.configure(bind=engine)
session  = session()

def create_db():
    # Crea la BD si no existe
    
    engine.execute("CREATE DATABASE IF NOT EXISTS {0}".format('shoppingCart'))
    engine.execute("USE {0}".format('shoppingCart'))

def init_db(create):
    if create:
        # Crea BD despues de levantar.
        create_db()

        # Crea todas las tablas en la BD, si ya exiten no las crea.
        Base.metadata.create_all(engine)
    else:
        Base.metadata.bind = engine
        engine.execute("USE {0}".format('shoppingCart'))

    print("---DB creada / Inicializada!---")

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
