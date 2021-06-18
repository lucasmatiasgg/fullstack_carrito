from flask import Blueprint
from flask import request, Response, json
from model.product import Product, save
from model.entityResponse import EntityResponse, EntityResponseEncoder
from sqlalchemy import update, delete, select
import constants
from config import session
from flask_cors import cross_origin

productController = Blueprint('productController', __name__)

@productController.route('/products/create', methods=['POST'])
def createProduct():
    if request.get_json():

        name = request.get_json().get('name')
        description = request.get_json().get('description')
        price = request.get_json().get('price')
        image = request.get_json().get('image')

        if name == None or description == None or price == None:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

        count = session.query(Product).filter_by(name=name).count()
        if  count > 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_ALREADY_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_ALREADY_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        
        product = Product()
        
        product.name = name
        product.description = description
        product.price = price
        product.image = image.encode('utf-8')

        save(product)

        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(response.__dict__),status=201)
    
    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


@productController.route('/products/getProductById/<int:id>')
def getProductByName(id):
    if id == None:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
        return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
    
    try:
        product = session.query(Product).filter_by(productId=id).first()
    except Exception as e:
        print(e)
        notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
        return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')
    
    if product != None:
        
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        responseObject = {}
        
        responseObject['status'] = json.loads(response.toJson())
        
        productsObj={}
        productsObj['productId'] = product.productId
        productsObj['name'] = product.name
        productsObj['description'] = product.description
        productsObj['price'] = product.price
        productsObj['image'] = product.image.decode('utf-8')
        responseObject['products'] = productsObj
        jsonResponse = json.dumps(responseObject)

        return Response(jsonResponse,status=200)
    
    notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
    return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')


#Este método actualiza todos los atributos de la tabla product.
#En caso de no recibir alguno de los atributos retorna un error.
@productController.route('/products/update/<int:id>', methods=['PUT'])
def updateProduct(id):

    if request.get_json() and id != None:
        description = request.get_json().get('description')
        price = request.get_json().get('price')
        name = request.get_json().get('name')

        count = session.query(Product).filter_by(productId=id).count()
        if  count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')

        if description == None or price == None or name == None:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

        stmt = (
            update(Product).
            where(Product.productId==id).
            values(name=name, description=description, price=price)
        )
        print(stmt)
        session.execute(stmt)
        session.commit()

        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(response.__dict__),status=201)
    
    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


@productController.route('/products/delete/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    if id == None:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
        return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
    
    count = session.query(Product).filter_by(productId=id).count()
    if  count == 0:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS, False)
        return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')
    
    stmt = (
        delete(Product).
        where(Product.productId==id)
    )
    print(stmt)
    session.execute(stmt)
    session.commit()
    
    response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
    return Response(json.dumps(response.__dict__),status=200)

@productController.route('/products/getAllProducts')
def getProducts():
    
    products = session.query(Product)
    responseObject = {}
    
    
    productList = []
    for product in products:    

        productsObj={}
        productsObj['productId'] = product.productId
        productsObj['name'] = product.name
        productsObj['description'] = product.description
        productsObj['price'] = product.price
        productsObj['image'] = product.image.decode('utf-8')

        productList.append(productsObj)
    

    if productList.count != 0:
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        
        
        responseObject['status'] = json.loads(response.toJson())
        responseObject['products'] = productList
        jsonResponse = json.dumps(responseObject)

        return Response(jsonResponse,status=200)

    notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
    return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')

def getPriceById(id):
    if id != None:
         product = session.query(Product).filter_by(productId=id).first()
         return product.price
    return 0