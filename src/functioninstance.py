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




    def getDict(self):
        posDict = {
                "x": 0,
                "y" : 0
            }
        oDict = self.function.getOptions()
        fDict = {
            "type" : self.function.getKnotenTyp(),
            "id" : "{}{}".format(self.function.getKnotenTyp(),self.fid),
            "name" : "{}{}".format(self.function.getKnotenTyp(),self.fid),
            "options" : [],
            "state" : {},
            "interfaces":[],
            "position" : posDict,
            "width" : 200,
            "twoColumn": False
        }
        fDict["options"].append(oDict)
        outputID = "out{}".format(self.fid)
        outputValueDict = {
            "id": outputID,
            "value": "null"
        } #from outputvalue
        outputDict = {
            "Output":outputValueDict
        }
        

        fDict["interfaces"].append(outputDict)
        for p in self.parameterList:
            fDict["interfaces"].append(p.getDict())
        return fDict

    def __init__(self, function, fid):
        self.function = function
        self.parameterList = list()
        self.fid = fid
        self.output = None
