import parameterinstance as pi
class parameter:

    def createParameterInstance(self, value):
        p = pi.parameterinstance(self, self.pid)
        self.pid = self.pid + 1
        return p

    def createOuput(self):
        p = pi.parameterinstance(self, self.pid)
        self.pid = self.pid + 1
        return p

    def getName(self):
        return self.name

    def getTyp(self):
        return self.typ

    def __init__(self, name, typ):
        self.name=name
        self.typ=typ
        self.pid = 0
    