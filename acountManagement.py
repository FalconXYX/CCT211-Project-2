import json
import acount
import stockRecord
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
def createAcount(username: str, password: str, name: str)-> acount.Acount:
    dict = {
        "username": username,
        "password": password,
        "name": name,
        "totalInvested": 0,
        "netWorth": 0,
        "stocks": []
    }
    with open('Acounts/'+username+'.json', 'w') as f:
        json.dump(dict, f)
    return acount.Acount(username, password, name, 0, 0, [])
def login(username: str, password: str):
    with open('Acounts/'+username+'.json') as f:
        data = json.load(f)
        if(checkPassword(data['password'], password)):
            #create stockRecord objects
            stocks = []
            for i in data['stocks']:
                stocks.append(stockRecord.StockRecord(i['symbol'], i['name'], i['shares'], i['purchasePrice']))

            #create acount object
            a = acount.Acount(data['username'], data['password'], data['name'], data['totalInvested'], data['netWorth'], stocks)
        else:
            return False,""

def checkPassword(answer: str, password: str) -> bool:
    return answer == password
    

