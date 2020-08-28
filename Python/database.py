# Database is a graph where each node is a user
class Database:
    def __init__(self, users=set()):
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
        # Nobody can manage the CEO, and cannot manage each other
        if userB.isCEO or userA is userB:
            return False
        # A user cannot manage someone who is directly or
        # indirectly managing them.
        if self.directOrIndirectManagers(userA, userB):
            return False
        userA.manages.add(userB)
        userB.managers.add(userA)
        return True

    # Check if userA is directly or indirectly managed by userB.
    def directOrIndirectManagers(self, userA, userB):
        # userB is a direct manager of userA
        if userB in userA.managers:
            return True
        # Any of the managers for B is an indirect manager for userA
        for managers in userA.managers:
            if self.directOrIndirectManagers(managers, userB):
                return True
        return False

    # Returns shortest route from user to CEO
    def connectToCEO(self, user):
        minSequence = [None for i in range(len(self.users))]
        curSequence = []
        def connectToCEOHelper(user, curSequence):
            nonlocal minSequence
            if user.isCEO:
                if len(curSequence) < len(minSequence):
                    minSequence = list(curSequence)
                return

            # Invalid
            if not user.isCEO and len(user.managers) == 0:
                minSequence = []
                return
            for manager in user.managers:
                curSequence.append(manager)
                connectToCEOHelper(manager, curSequence)
                curSequence.pop()

        connectToCEOHelper(user, curSequence)
        return minSequence



