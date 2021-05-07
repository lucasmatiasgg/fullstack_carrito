class Credential:
id: 0
username: ""
password: ""

def __init__(self, username, password):
        self.username = username
        self.password = password

# Dejo comentado proque no deberiamos imprimir las credenciales de un usuario.    
#def __str__(self):
#    return self.username + ' ' + self.password