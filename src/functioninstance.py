import konstantenManager as km
import funktion

class functioninstance:
    
    def getOutputTyp(self):
        self.function.getOutputTyp()

    def addParameterInstance(self, p):
        self.parameterList.append(p)

    def setOutput(self, output):
        self.output = output
    
    def getFunktion(self):
        return self.function

    def getInterfaces(self):
        interfaces='"state": { },"interfaces": ['
        if (self.function.knotentyp =="MathNode"):
            interfaces=interfaces + '["Value 1",{"id":"' +self.function.functionName + self.fid +'v1","value": 0}],'
            interfaces=interfaces + '["Value 2",{"id":"' +self.function.functionName + self.fid +'v2","value": 0}],'
            interfaces=interfaces + '["Result",{"id":"' +self.function.functionName + self.fid +'r","value": null}]],'
            return interfaces
   

    def getDict(self):

        dictHead = '"type":"{}","id":"{}{}","name":"{}",'.format(self.function.getKnotenTyp(),self.function.getKnotenTyp(),self.fid,self.function.getKnotenTyp(),self.fid)
        options = self.function.getOption()
        interfaces = self.getInterfaces
        dictend =  '"position": {"x": 0,"y": 0}, "width": 200, "twoColumn": false}'
        dictHead=dictHead+options+interfaces+dictend
        return dictHead

    def __init__(self, function, fid):
        self.function = function
        self.parameterList = list()
        self.fid = fid
        self.output = None
