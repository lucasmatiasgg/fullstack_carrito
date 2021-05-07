class User:
    id= 0
    amount= 0
    quantity= 0

    def __init__(self, amount, quantity):
        self.amount = amount
        self.quantity = quantity
    
    def __str__(self):
        return self.amount + ' ' + self.quantity