import json
from user import User
from database import Database
from testPlan import TestPlan

def readDataToDB(filename, database, usersList):
    file = open(filename)
    data = json.load(file)
    for user in data["users"]:
        newUser = User(user["name"], user["email"], user["phoneNumber"], user["department"])
        database.addUser(newUser)
        usersList.append(newUser)

def printDatabase(database):
    for user in database.users:
        print(user)
        print("Managers: ")
        for m in user.managers:
            print("    " + m.name)
        print("Manages: ")
        for m in user.manages:
            print("    " + m.name)

def main():
    filename = "database.json"
    database = Database()
    usersList = []
    readDataToDB(filename, database, usersList)

    # LBJ is manager
    usersList[0].isCEO = True

    # LBJ manages KD and SC
    database.setManagerFor(usersList[0], usersList[1]) # KD
    database.setManagerFor(usersList[0], usersList[2]) # SC

    # SC manages RW and KI
    database.setManagerFor(usersList[2], usersList[4]) # KI
    database.setManagerFor(usersList[2], usersList[5]) # RW

    # KD manages KI and SC
    database.setManagerFor(usersList[1], usersList[5]) # KI
    database.setManagerFor(usersList[1], usersList[2]) # SC

    # LBJ manages JH
    database.setManagerFor(usersList[0], usersList[3]) # JH

    # JH manages RW
    database.setManagerFor(usersList[3], usersList[4]) # RW

    # KD, RW, and KI manages DL
    database.setManagerFor(usersList[4], usersList[6]) # RW
    database.setManagerFor(usersList[1], usersList[6]) # KD
    database.setManagerFor(usersList[5], usersList[6]) # KI

    # printDatabase(database)

    for user in usersList:
        d = len(database.connectToCEO(user))
        print("Shortest route from " + user.name + " to CEO:", d)


    test1 = TestPlan(usersList[6])
    # test1.prettyPrint()

    test1.approve(usersList[2]) # Will fail
    test1.approve(usersList[6])
    # test1.prettyPrint()

    test1.approve(usersList[6]) # Will fail
    test1.approve(usersList[1])
    # test1.prettyPrint()

    test1.approve(usersList[0])
    test1.prettyPrint()

main()

