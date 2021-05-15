from flask import Blueprint
from flask import request, Response, json
from model.user import User, save
from model.credential import Credential
from model.entityResponse import EntityResponse
from sqlalchemy import update, delete
import constants
from config import session
from sqlalchemy.sql.expression import func

userController = Blueprint('userController', __name__)

@userController.route('/users/create', methods=['POST'])
def createUser():
    if request.get_json():
        first = request.get_json().get('first_name')
        last = request.get_json().get('last_name')
        userName = request.get_json().get('user_name')
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
        maxId = session.query(func.max(User.user_id)).scalar()
        print('maxId: ', maxId)

        if maxId != None:
            newCredential.user_id = maxId + 1
        else:
            newCredential.user_id = 1

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
        user = session.query(User).filter_by(user_id = id).first()
        print(user)
    except Exception as e:
        print(e)
        notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
        return Response(json.dumps(notFoundResponse.__dict__), status = 404, mimetype = 'application/json')
    
    if user != None:
        print(user.__dict__)
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(user.users_to_dict()), status = 200)

    notFoundResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_NOT_CONTENT, constants.RESPONSE_MESSAGE_ERROR_NOT_FOUND, False)
    return Response(json.dumps(notFoundResponse.__dict__), status=404, mimetype='application/json')


@userController.route('/users/update/<int:id>', methods=['PUT'])
def updateUser(id):

    if request.get_json and id != None:
        first = request.get_json().get('first_name')
        last = request.get_json().get('last_name')
    
        count = session.query(User).filter_by(user_id = id).count()

        if count == 0:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_USER_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_USER_NOT_EXISTS, False)
            return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')
        
        if first == None or last == None:
            errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_PARAMS_REQUIRED, constants.RESPONSE_MESSAGE_ERROR_PARAMS_REQUIRED, False)
            return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')
        

        stmt = (
                update(User).
                where(User.user_id==id).
                values(firstName=first, lastName = last)
            )
        print(stmt)
        session.execute(stmt)
        session.commit()
        response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
        return Response(json.dumps(response.__dict__),status=201)

    errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_BAD_REQUEST, constants.RESPONSE_MESSAGE_ERROR_BAD_REQUEST, False)
    return Response(json.dumps(errorResponse.__dict__), status=400, mimetype='application/json')


@userController.route('/users/delete/<int:id>', methods=['DELETE'])
def deleteUser(id):
    if id  == None:
        errorResponse = EntityResponse(constants.RESPONSE_CODE_ERROR_USER_NOT_EXISTS, constants.RESPONSE_MESSAGE_ERROR_USER_NOT_EXISTS, False)
        return Response(json.dumps(errorResponse.__dict__), status=404, mimetype='application/json')

    stmt = (
        delete(User).
        where(User.user_id == id)
    )

    print (stmt)
    session.execute(stmt)
    session.commit()

    response = EntityResponse(constants.RESPONSE_CODE_OK, constants.RESPONSE_MESSAGE_OK, True)
    return Response(json.dumps(response.__dict__), status = 200)
