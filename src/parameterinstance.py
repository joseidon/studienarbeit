class parameterinstance:

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getParamter(self):
        return self.parameter

    def getDict(self):
        paramDict = {
            "id" : self.pid,
            "value" : "null"
        }
        pDict = {
            self.parameter.getName() : paramDict
        }
        return pDict


    def __init__(self, parameter, pid):
        self.pid = pid
        self.parameter = parameter
        self.value = None