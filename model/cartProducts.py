import json
from json import JSONEncoder

class CartProducts:
    name = ""
    quantity = 0
    price = 0.0
    amount = 0.0

    def __init__(self, name, quantity, price, amount):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.amount = amount

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class CartProductsEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__
