class managermanager:

    def setFunctionManager(self, functionManager):
        self.functionManager = functionManager

    def setVariablenManager(self, variablenManager):
        self.variablenManager = variablenManager

    def getFunctionManager(self):
        return self.functionManager

    def getVariablenManager(self):
        return self.variablenManager


    def __init__(self):
        print("manager created")
        self.functionManager = None
        self.variablenManager = None