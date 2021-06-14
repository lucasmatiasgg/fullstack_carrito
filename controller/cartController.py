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
from model.cartProducts import CartProducts, CartProductsEncoder
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
        

        count = session.query(Product).filter_by(productId=idProduct).count()
        if count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        
        count = session.query(User).filter_by(userId=idUser).count()
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
            responseObject = {}

            response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
            responseObject['status'] = json.loads(response.toJson())
            responseObject['idCart'] = idCart
            jsonResponse = json.dumps(responseObject)
            return Response(jsonResponse,status=201)
    
    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


@cartController.route('/carts/getProductsByCartId/<int:id>')
def getProductsByCartId(id):
    if id != None:

        results =  session.query(Item.quantity, Product.name, Product.price, Item.amount). \
            select_from(Product).join(Item).join(order_item). \
            filter(order_item.columns.cartId == id).all()

        print ("......................................results......................................")
        print (results)
        print ("......................................results......................................")
        orderItemList = []


        for products in results:
            name = products.name
            quantity = products.quantity
            price = products.price
            amount = products.amount

            cartProducts = CartProducts(name, quantity, price, amount)
            
            cartProductsJSONData = json.loads(cartProducts.toJson())
            print("\ncartProductsJSONData")
            print(cartProductsJSONData)
            print(type(cartProductsJSONData))
            orderItemList.append(cartProductsJSONData)
        
        
        print("orderItemList")
        print(orderItemList)

            
        if orderItemList.count != 0:
            responseObject = {}
            response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        
            responseObject['status'] = json.loads(response.toJson())
            responseObject['products'] = orderItemList
            jsonResponse = json.dumps(responseObject)

            return Response(jsonResponse,status=200)

        notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
        return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')
    

    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


def addNewItem(idProduct, quantity, totalItem):
    if idProduct != None and quantity > 0:
        
        
        maxId = session.query(func.max(Item.item_id)).scalar()
        if maxId == None:
            maxId = 0

        item = Item()
        item.item_id = maxId + 1
        item.productId = idProduct
        item.quantity = quantity
        item.amount = totalItem

        save(item)
        return item.item_id
    return 1
    
def getCartIdByUser(idUser):
    if idUser != None:
        historyCart = session.query(history_cart).filter_by(userId=idUser).first()
         
        if historyCart != None:
            print("getCartIdByUser - historyCart")
            print(historyCart.cartId)
            return historyCart.cartId
        return 0
    return -1

def createCartByUser(idUser):
    if idUser != None:
        maxId = session.query(func.max(Cart.cartId)).scalar()
        print("createCartByUser - MaxID: " + str(maxId))
        if maxId == None:
            maxId = 0

        print("MaxID: " + str(maxId))
        cart = Cart()
        cart.cartId = maxId + 1
        cart.totalAmount = 0

        save(cart)

        # Una vez creado el carrito hay que asociarlo a la tabla history_cart
        user = User()
        user = session.query(User).filter_by(userId=idUser).first()
        cart.userRelation.append(user)
        session.commit()
        return cart.cartId

    return -1

def updateCart(idCart, idItem, totalItem):
    if idCart != None:
        cart = Cart()
        cart = session.query(Cart).filter_by(cartId=idCart).first()

        newAmount = cart.totalAmount + totalItem

        stmt = (
            update(Cart).
            where(Cart.cartId == idCart).
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


@cartController.route('/carts/deleteItem/<int:idProduct>', methods=['DELETE'])
def deleteItem(idProduct):
    if idProduct  == None:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS, False)
        return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')

    idToDelete =  session.query(Item.item_id). \
                    select_from(Item).join(order_item). \
                    filter(order_item.columns.item_id == Item.item_id and \
                    Item.productId == idProduct and order_item.columns.cartId == 2).first()

    print ('==============')
    print (idToDelete)
    print ('==============')
    
    stmtDelete = (
        delete(Item).
        where(Item.productId == idToDelete)
    )

    print ('==============')
    print (stmtDelete)
    print ('==============')
    
    # session.execute(stmtDelete)
    # session.commit()
    

    response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
    return Response(json.dumps(response.__dict__), status = 200)
