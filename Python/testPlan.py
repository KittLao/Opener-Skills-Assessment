class TestPlan:
    def __init__(self, author):
        # Maps the stage to whoever approved it and people who
        # are eligible to approve it.
        self.stages = {"Low": [None, set()], 
                "Moderate": [None, set()], 
                "High": [None, set()], 
                "Finished": []
                }
        self.author = author
        # Always initially Low
        self.currentStage = "Low"
        self.getApprovalsLow(self.stages["Low"][1])
        self.getApprovalsModerate(self.stages["Moderate"][1])
        self.getApprovalsHigh(self.author.managers, self.stages["High"][1])

    def prettyPrint(self):
        print("The current stage for this test plan is:", self.currentStage)
        for stage in self.stages:
            if stage == "Finished":
                break
            print("--------------------------------\n")
            print("Stage " + stage + ":")
            if self.stages[stage][0]:
                print("Has been approved by: ", self.stages[stage][0])
            else:
                print("Has not been approved yet. Here are the people eligible to approve:")
                for user in self.stages[stage][1]:
                    print(user)
            print("--------------------------------\n")

    def approve(self, approver):
        # Already finished
        if self.currentStage == "Finished":
            return True
        if approver in self.stages[self.currentStage][1]:
            self.stages[self.currentStage][0] = approver
            # Update stages
            if self.currentStage == "Low":
                self.currentStage = "Moderate"
            elif self.currentStage == "Moderate":
                self.currentStage = "High"
            else:
                self.currentStage = "Finished"
            return True
        # Cannot approve
        return False

    def getApprovalsLow(self, approvers=set()):
        approvers.add(self.author)

    def getApprovalsModerate(self, approvers=set()):
        approvers.update(self.author.managers)

    def getApprovalsHigh(self, managers, approvers=set()):
        for manager in managers:
            approvers.update(manager.managers)
            self.getApprovalsHigh(manager.managers, approvers)