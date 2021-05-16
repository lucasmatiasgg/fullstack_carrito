from flask import Blueprint
from flask import request, Response, json
from model.product import Product, save
from model.entityResponse import EntityResponse
from sqlalchemy import update, delete, select
import constants
from config import session

productController = Blueprint('productController', __name__)

@productController.route('/products/create', methods=['POST'])
def createProduct():
    if request.get_json():

        name = request.get_json().get('name')
        description = request.get_json().get('description')
        price = request.get_json().get('price')

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
        product = session.query(Product).filter_by(product_id=id).first()
    except Exception as e:
        print(e)
        notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
        return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')
    
    if product != None:
        print(product.__dict__)
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(product.products_to_dict()),status=200)
    
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

        count = session.query(Product).filter_by(product_id=id).count()
        if  count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')

        if description == None or price == None or name == None:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

        stmt = (
            update(Product).
            where(Product.product_id==id).
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
    
    count = session.query(Product).filter_by(product_id=id).count()
    if  count == 0:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PRODUCT_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_PRODUCT_NOT_EXISTS, False)
        return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')
    
    stmt = (
        delete(Product).
        where(Product.product_id==id)
    )
    print(stmt)
    session.execute(stmt)
    session.commit()
    
    response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
    return Response(json.dumps(response.__dict__),status=200)

@productController.route('/products/getAllProducts')
def getProducts():
    
    # TODO Hay que usar paginacion
    
    products = session.query(Product)
    productList = []
    for product in products:
        productList.append(json.dumps(product.products_to_dict()))
        
    print(productList)

    if productList.count != 0:
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        return Response(productList,status=200)

    notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
    return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')

def getPriceById(id):
    if id != None:
         product = session.query(Product).filter_by(product_id=id).first()
         print("getPriceById - PRODUCT")
         print(product)
         return product.price
    return 0