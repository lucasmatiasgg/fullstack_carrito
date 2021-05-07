class Product:
    id= 0
    description= ""
    price= 0

    def __init__(self, description, price):
        self.description = description
        self.price = price
    
    def __str__(self):
        return self.description + ' ' + self.price