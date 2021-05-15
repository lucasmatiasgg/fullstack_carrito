from flask import Blueprint
from flask import request, Response, json
from config import session
from sqlalchemy import update, delete, select
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import aliased
from model.product import Product
from model.item import Item
from model.entityResponse import EntityResponse
from model.historyCart import history_cart
from model.orderItem import order_item
from model.cart import Cart, save
from controller.productController import getPriceById
from model.user import User
import constants


cartController = Blueprint('cartController', __name__)

@cartController.route('/carts/addProductToCart', methods=['POST'])
def createProduct():
    if request.get_json():

        idProduct = request.get_json().get('idProduct')
        quantity = request.get_json().get('quantity')
        idUser = request.get_json().get('idUser')

        if idProduct == None or quantity == None or quantity < 1 or idUser == None:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        

        count = session.query(Product).filter_by(product_id=idProduct).count()
        if count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        
        count = session.query(User).filter_by(user_id=idUser).count()
        if count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_USER_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_USER_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

        unitPrice = getPriceById(idProduct)
        print(idProduct)
        print(quantity)
        print(unitPrice)
        totalItem = quantity * unitPrice

        if  unitPrice == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_GENERIC, constants.RESPONSE_MESSAGE_ERROR_GENERIC, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        
        # Agregamos un nuevo item con los datos ingresados
        idItem = addNewItem(idProduct, quantity, totalItem)

        # Buscamos el carrito del usuario
        idCart = getCartIdByUser(idUser)
        
        print("addProductToCart-idCart:" + str(idCart))
        # Si idCart es == 0 es porque no existe el carrito asociado al usuario y lo tenemos que crear
        if idCart == 0:
            idCart = createCartByUser(idUser)

        result = updateCart(idCart, idItem, totalItem)

        if result == 0:
            response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
            return Response(json.dumps(response.__dict__),status=201)
    
    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


# @cartController.route('/carts/getProductsByCartId/<int:id>')
# def getProductsByCartId(id):
#     #TODO Pendiente de buscar como hacer la query con sqlalchemy

def addNewItem(idProduct, quantity, totalItem):
    if idProduct != None and quantity > 0:
        
        
        maxId = session.query(func.max(Item.item_id)).scalar()
        if maxId == None:
            maxId = 0

        item = Item()
        item.item_id = maxId + 1
        item.product_id = idProduct
        item.quantity = quantity
        item.amount = totalItem

        save(item)
        return item.item_id
    return 1
    
def getCartIdByUser(idUser):
    if idUser != None:
        historyCart = session.query(history_cart).filter_by(user_id=idUser).first()
         
        if historyCart != None:
            print("getCartIdByUser - historyCart")
            print(historyCart.cart_id)
            return historyCart.cart_id
        return 0
    return -1

def createCartByUser(idUser):
    if idUser != None:
        maxId = session.query(func.max(Cart.cart_id)).scalar()
        print("createCartByUser - MaxID: " + str(maxId))
        if maxId == None:
            maxId = 0

        print("MaxID: " + str(maxId))
        cart = Cart()
        cart.cart_id = maxId + 1
        cart.totalAmount = 0

        save(cart)

        # Una vez creado el carrito hay que asociarlo a la tabla history_cart
        user = User()
        user = session.query(User).filter_by(user_id=idUser).first()
        cart.userRelation.append(user)
        session.commit()
        return cart.cart_id

    return -1

def updateCart(idCart, idItem, totalItem):
    if idCart != None:
        cart = Cart()
        cart = session.query(Cart).filter_by(cart_id=idCart).first()

        newAmount = cart.totalAmount + totalItem

        stmt = (
            update(Cart).
            where(Cart.cart_id == idCart).
            values(totalAmount=newAmount)
        )
        session.execute(stmt)
        session.commit()

        item = Item()
        item = session.query(Item).filter_by(item_id=idItem).first()
        cart.itemRelation.append(item)
        session.commit()

        return 0
    return -1