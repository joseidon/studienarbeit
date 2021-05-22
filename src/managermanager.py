class managermanager:

    def setFunctionManager(self, functionManager):
        self.functionManager = functionManager

    def setKonstantenManager(self, konstantenManager):
        self.konstantenManager = konstantenManager

    def setVariablenManager(self, variablenManager):
        self.variablenManager = variablenManager

    def getFunctionManager(self):
        return self.functionManager

    def getVariablenManager(self):
        return self.variablenManager
    
    def getKonstantenManager(self):
        return self.konstantenManager


    def __init__(self):
        print("manager created")
        self.functionManager = None
        self.konstantenManager = None
        self.variablenManager = None