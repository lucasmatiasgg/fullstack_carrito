from flask import Blueprint
from flask import request, Response, json
from model.product import Product, save
from model.entityResponse import EntityResponse
from model.constants import RESPONSE_CODE_OK, RESPONSE_MESSAGE_OK, RESPONSE_CODE_ERROR_PARAMS_REQUIRED, RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED
from model.constants import RESPONSE_CODE_ERROR_BAD_REQUEST, RESPONSE_MESSAGE_ERROR_BAD_REQUEST, RESPONSE_MESSAGE_ERROR_NOT_FOUND, RESPONSE_CODE_ERROR_NOT_CONTENT
from config import session
# from model.products_to_dict import ProductsToDict

productController = Blueprint('productController', __name__)

@productController.route('/products/create', methods=['POST'])
def createProduct():
    if request.get_json():

        name = request.get_json().get('name')
        description = request.get_json().get('description')
        price = request.get_json().get('price')

        if name == None or description == None or price == None:
            errorResponse = EntityResponse(RESPONSE_CODE_ERROR_PARAMS_REQUIRED, RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

        product = Product()
        
        product.name = name
        product.description = description
        product.price = price

        save(product)

        response = EntityResponse(RESPONSE_CODE_OK, RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(response.__dict__),status=201)
    
    errorResponse = EntityResponse(RESPONSE_CODE_ERROR_BAD_REQUEST, RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


@productController.route('/products/getProductByName/<string:name>')
def getProductByName(name):
    if name == None:
        errorResponse = EntityResponse(RESPONSE_CODE_ERROR_PARAMS_REQUIRED, RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
        return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
    
    try:
        product = session.query(Product).filter_by(name=name).first()
    except Exception as e:
        print(e)
        notFoundResponse = EntityResponse(RESPONSE_CODE_ERROR_NOT_CONTENT, RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
        return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')
    
    if product != None:
        print(product.__dict__)
        response = EntityResponse(RESPONSE_CODE_OK, RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(product.products_to_dict()),status=200)
    
    notFoundResponse = EntityResponse(RESPONSE_CODE_ERROR_NOT_CONTENT, RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
    return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')


@productController.route('/products/deleteProduct', methods=['DELETE'])
def deleteProduct():
    return 'ok'