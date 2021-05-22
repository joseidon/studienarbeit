import functioninstance as fi
import parameter 

class funktion:

    def createFunctionInstance(self, arguements):
        f=fi.functioninstance(self, self.fid)
        self.fid=self.fid+1
        values = arguements.split(',')
        i=0
        for p in self.parameterList:
            newP = p.createParameterInstance(values[i])
            f.addParameterInstance(newP)
            i=i+1
        newO = p.createOuput()
        f.setOutput(newO)
        self.nodeList.append(f)
        return f

    def getDict(self):
        dictList = list()
        for f in self.nodeList:
            dictList.append(f.getDict())
        return dictList

    def setOutput(self, output):
        self.output = output

    def getName(self):
        return self.functionName

    def getOutputTyp(self):
        return self.output.getTyp()

    def getKnotenTyp(self):
        return self.knotentyp

    def getOptions(self):
        if (self.knotentyp =="MathNode"):
            mathnodeList = ["Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute"]
            print('Mathnode')
           # midDict = 
            #oDict= {
            #    [
            #        "Operation",
            #        [
#                        "selected": self.functionName,
            #            "items": mathnodeList
            #        ]
            #    ]
        #}
        #fDict["options"].append(oDict)
        #print(oDict)
        #return oDict



    def __init__(self, functionName, knotentyp, manager):
        self.functionName = functionName
        self.parameterList=list()
        self.knotentyp=knotentyp
        self.output  = None
        self.nodeList = list()
        self.manager = manager
        self.fid = 0
