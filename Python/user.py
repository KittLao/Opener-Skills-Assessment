# User is a node where it has access to who it directly
# manages and who directly manages them
class User:
    def __init__(self, name, email, phoneNumber, department, isCEO=False):
        # Basic info
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.department = department
        self.isCEO = isCEO
        # Pointers to managers and who it manages
        self.managers = set()
        self.manages = set()

    def __repr__(self):
        userRepr = '\n'
        userRepr += "Name: " + self.name + '\n'
        userRepr += "Email: " + self.email + '\n'
        userRepr += "Phone Number: " + self.phoneNumber + '\n'
        userRepr += "Department: " + self.department + '\n'
        return userRepr
