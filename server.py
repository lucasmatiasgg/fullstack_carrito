from flask import Flask
import config
import sys
from controller.userController import userController
from dataBaseModel.product import Product
from dataBaseModel.user import User
from dataBaseModel.credential import Credential
from dataBaseModel.cart import Cart
from dataBaseModel.historyCart import association_table

app = Flask(__name__, instance_relative_config=True)

#config
app.config.from_object('config')
app.config.from_pyfile('config.py')


#Blueprints
app.register_blueprint(userController)



# Si para levantar el server le pasamos createdb entonces dropea la BD y la crea de nuevo.
if len(sys.argv) > 1 and 'createdb' == sys.argv[1]:
    config.drop_db()
    config.init_db()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
