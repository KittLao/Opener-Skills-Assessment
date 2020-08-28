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
        self.managers = {}
        self.manages = {}

    def __repr__(self):
        userRepr = '\n'
        userRepr += self.name + '\n'
        userRepr += self.email + '\n'
        userRepr += self.phoneNumber + '\n'
        userRepr += self.department + '\n'
        return userRepr
