from flask import Blueprint
from flask import request, Response, json
from model.user import User, save
from model.credential import Credential
from model.entityResponse import EntityResponse
from sqlalchemy import update, delete
import constants
from config import session
from sqlalchemy.sql.expression import func
from controller.cartController import getCartIdByUser

userController = Blueprint('userController', __name__)

@userController.route('/users/create', methods=['POST'])
def createUser():
    if request.get_json():
        first = request.get_json().get('firstName')
        last = request.get_json().get('lastName')
        userName = request.get_json().get('userName')
        password = request.get_json().get('password')

        if first == None or last == None or userName == None or userName == "":
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        

        count = session.query(Credential).filter_by(userName=userName).count()

        if  count > 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_USERNAME_ALREADY_EXISTS, constants.RESPONSE_MESSAGE_ERROR_USERNAME_ALREADY_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

        newUser = User()
        newUser.lastName = last
        newUser.firstName = first

        newCredential = Credential()
        newCredential.userName = userName
        newCredential.password = password
        maxId = session.query(func.max(User.userId)).scalar()
        print('maxId: ', maxId)

        if maxId != None:
            newCredential.userId = maxId + 1
        else:
            newCredential.userId = 1

        newCredential.userName = userName
        newCredential.password = password

        save(newUser)
        save(newCredential)
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(response.__dict__), status=201)
    
    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

@userController.route('/users/getUserById/<int:id>')
def getUserById(id):
    if id == None:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
        return Response(json.dumps(errorResponse.__dict__), status = 400, mimetype = 'application/json')

    try:
        user = session.query(User).filter_by(userId = id).first()
        print(user)
    except Exception as e:
        print(e)
        notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
        return Response(json.dumps(notFoundResponse.__dict__), status = 404, mimetype = 'application/json')
    
    if user != None:
        print(user.__dict__)
        responseObject = {}
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        
        responseObject['status'] = json.loads(response.toJson())
        responseObject['userInfo'] = user.users_to_dict()

        jsonResponse = json.dumps(responseObject)
        return Response(jsonResponse,status=200)

    notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
    return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')


@userController.route('/users/update/<int:id>', methods=['PUT'])
def updateUser(id):

    if request.get_json and id != None:
        first = request.get_json().get('firstName')
        last = request.get_json().get('lastName')
        oldPassword = request.get_json().get('oldPassword')
    
        count = session.query(User).filter_by(userId = id).count()

        if count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_USER_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_USER_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')
        
        if first == None or last == None or oldPassword == None:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        
        user = session.query(Credential).filter_by(userId = id).first()
        print(user.password)
        print("Antes de validar pw")
        if(user.password == oldPassword):
            print("Estoy dentro del if. Ya valide la contraseña")
            stmt = (
                    update(User).
                    where(User.userId==id).
                    values(firstName=first, lastName = last)
                )
            #print(stmt)
            session.execute(stmt)
            print("Ejecute stmt")
            session.commit()
            response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
            return Response(json.dumps(response.__dict__),status=200)
            
        else:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_INVALID_PASSWORD, constants.RESPONSE_MESSAGE_ERROR_INVALID_PASSWORD, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


@userController.route('/users/delete/<int:id>', methods=['DELETE'])
def deleteUser(id):
    if id  == None:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_USER_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_USER_NOT_EXISTS, False)
        return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')

    stmtCredential = (
        delete(Credential).
        where(Credential.userId == id)
    )

    stmtUser = (
        delete(User).
        where(User.userId == id)
    )

    session.execute(stmtCredential)
    session.execute(stmtUser)
    session.commit()

    response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
    return Response(json.dumps(response.__dict__), status = 200)

@userController.route('/users/validateCredentials', methods=['POST'])
def validateCredentials():
    if request.get_json():
        userName = request.get_json().get('userName')
        password = request.get_json().get('password')
        responseObject = {}

        if userName == None or password == None :
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        

        try:
            user = session.query(Credential).filter_by(userName = userName).first()
            print(user)
            idCart = getCartIdByUser(user.userId)
            print('IDCART', idCart)
        except Exception as e:
            print(e)
            
            notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_INVALID_CREDENTIALS, constants.RESPONSE_MESSAGE_ERROR_INVALID_CREDENTIALS, False)
            responseObject['status'] = json.loads(notFoundResponse.toJson())
            jsonResponse = json.dumps(responseObject)
            return Response(jsonResponse,status=200)
        
        if user != None and user.password == password:

            response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
            responseObject['status'] = json.loads(response.toJson())
            responseObject['userId'] = user.userId
            responseObject['cartId'] = idCart
            jsonResponse = json.dumps(responseObject)

            return Response(jsonResponse,status=200)
        
        response = EntityResponse(constants.RESPONSE_CODE_ERROR_INVALID_CREDENTIALS, constants.RESPONSE_MESSAGE_ERROR_INVALID_CREDENTIALS, False)
        responseObject['status'] = json.loads(response.toJson())
        jsonResponse = json.dumps(responseObject)
        return Response(jsonResponse,status=200)
    
    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

@userController.route('/users/updatePassword/<int:id>', methods=['PUT'])
def updatePassword(id):

    if request.get_json and id != None:
        newPassword = request.get_json().get('newPassword')
        oldPassword = request.get_json().get('oldPassword')
    
        count = session.query(User).filter_by(userId = id).count()

        if count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_USER_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_USER_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')
        
        if  newPassword == None or oldPassword == None:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        
        user = session.query(Credential).filter_by(userId = id).first()
        print(user.password)
        print("Antes de validar pw")
        if(user.password == oldPassword):
            print("Estoy dentro del if. Ya valide la contraseña")

            stmtPw = (
                update (Credential).
                where(Credential.userId == id).
                values(password = newPassword)
            )
            session.execute(stmtPw)
            print("Ya ejecute stmtPw")
            session.commit()
            response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
            return Response(json.dumps(response.__dict__),status=200)
            
        else:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_INVALID_PASSWORD, constants.RESPONSE_MESSAGE_ERROR_INVALID_PASSWORD, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')

    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')