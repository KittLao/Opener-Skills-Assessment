import json
from user import User
from database import Database
from testPlan import TestPlan

def readDataToDB(filename, database):
    file = open(filename)
    data = json.load(file)
    for user in data["users"]:
        newUser = User(user["name"], user["email"], user["phoneNumber"], user["department"])
        database.addUser(newUser)

def printDatabase(database):
    for user in database.users:
        print(user)
        print("Managers: ")
        for m in user.managers:
            print(m.name)
        print("Manages: ")
        for m in user.manages:
            print(m.name)

def main():
    filename = "database.json"
    database = Database()
    readDataToDB(filename, database)

    printDatabase(database)



main()

