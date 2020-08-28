# Database is a graph where each node is a user
class Database:
    def __init__(self, users={}):
        self.users = users

    def addUser(self, user):
        if user in self.users:
            return False
        self.users.add(user)
        return True

    def removeUser(self, user):
        if user not in self.users:
            return False
        # Remove user for anyone who manages them
        for managers in user.managers:
            managers.manages.remove(user)
        # Remove user for anyone who is managed by them
        for manages in user.manages:
            manages.managers.remove(user)
        # User who is not in database should not be managed by
        # anyone and should not be managing anyone.
        user.manages = {}
        user.managers = {}
        self.users.remove(user)
        return True

    # userA manages userB.
    def setManagerFor(self, userA, userB):
        # Both users need to exist in database
        if userA not in self.users or userB not in self.users:
            return False
        # Nobody can manage the CEO
        if userB.isCEO:
            return False
        # A user cannot manage someone who is directly or
        # indirectly managin them.
        if self.directOrIndirectManagers(userA, userB):
            return False
        userA.manages.add(userB)
        userB.managers.add(userA)

    # Check if userA is directly or indirectly managed by userB.
    def directOrIndirectManagers(self, userA, userB):
        if userA in userB.manages:
            return True
        for managers in userB.managers:
            if self.directOrIndirectManagers(userA, managers):
                return True
        return False

    def connectToCEO(self, user, minSequence=0):
        if user.isCEO:
            return minSequence
        optSequence = len(self.users)
        for manager in user.managers:
            sequence = self.connectToCEO(manager, minSequence + 1)
            optSequence = min(optSequence, sequence)
        return optSequence



