import json
# An acount is made up of a username,a password,  a name, total invested,net worth, and a list of stocks
"""
Instuctions on how to use:
first call checkExistinAcount() to check if the acount exists

1. If you are trying to login and the acount exists call login if that returns false that means 
the password is incorrect otherwise you will get back true and the acount object and can proceed to the next step
2. If you are trying to create a new acount if the acount does not exist call createAcount() and pass in the username, password, and name
it will return the acount object
"""
def checkExistinAcount(username: str) -> bool:
    #check if there is a file with the username.json in the Acounts folder
    try:
        with open('Acounts/'+username+'.json') as f:
            return True
    except:
        return False
def createAcount():
    pass
def login():
    pass
def checkPassword():
    pass

