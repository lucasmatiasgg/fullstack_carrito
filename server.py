from flask import Flask
import config
import sys
from controller.userController import userController
from controller.productController import productController
from model.product import Product
from model.user import User
from model.credential import Credential
from model.cart import Cart
from model.historyCart import association_table
from model.item import Item
from model.orderItem import association_table
from model.buyOrder import BuyOrder

app = Flask(__name__, instance_relative_config=True)

#config
app.config.from_object('config')
app.config.from_pyfile('config.py')


#Blueprints
app.register_blueprint(userController)
app.register_blueprint(productController)


# Si para levantar el server le pasamos createdb entonces dropea la BD y la crea de nuevo.
if len(sys.argv) > 1 and 'createdb' == sys.argv[1]:
    config.drop_db()
    config.init_db(True)
else:
    config.init_db(False)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
