class Engine:

    def __init__(self,engineNum,numCylinders):
        self.eN=engineNum
        self.nC=numCylinders

    def generateTorque(self,fuel):
        return self.nC*fuel/10;