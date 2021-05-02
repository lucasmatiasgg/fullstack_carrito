class Product:
    id= 0
    firstName= ""
    lastName= ""

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName