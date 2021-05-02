from flask import Blueprint

userController = Blueprint('userController', __name__)

@userController.route('/test', methods=['POST'])
def test():
    return 'ok'