from typing import ValuesView
from einlesen import getDict
import functioninstance as fi
import parameter 

class funktion:

    def createFunctionInstance(self, name, arguements, manager):
        if(self.knotentyp=='OutputNode'):
            f=self.createOutputInstance(name, arguements, manager)
            return f
        f=fi.functioninstance(self, self.fid, name)
        #print(name)
        self.fid=self.fid+1
        values = arguements.split(',')
        i=0
        for p in self.parameterList:
            newP = p.createParameterInstance(values[i], manager)
            f.addParameterInstance(newP)
            i=i+1
        newO = self.output.createOuput(name, manager)
        f.setOutput(newO)
        self.nodeList.append(f)
        return f

    def createOutputInstance(self,name, arguements, manager):
        f=fi.functioninstance(self, self.fid, name)
        #print(name)
        self.fid=self.fid+1
        values = arguements.split(',')
        i=0
        for p in self.parameterList:
            newP = p.createParameterInstance(values[i], manager)
            f.addParameterInstance(newP)
            i=i+1
        f.setLabel(values[1])
        self.nodeList.append(f)
        #print(f.getDict())
        return f

    def getDict(self, first):
        dictList = ""
        for f in self.nodeList:
            if (first!=True):
                dictList=dictList+","
            first=False
            dictList=dictList + f.getDict()
        return dictList

    def setOutput(self, output):
        self.output = output

    def getName(self):
        return self.functionName

    def getOutputTyp(self):
        return self.output.getTyp()

    def getKnotenTyp(self):
        return self.knotentyp
    
    
    def getOption(self, f):
        options='"options":['
        midpart=''
        if(self.knotentyp=='OutputNode'):
            label = f.getLabel()
            midpart= '["Label","{}"]'.format(str(label))
        if (self.knotentyp =="MathNode"):
            midpart='["Operation",{"selected":"'
            midpart=midpart+self.functionName
            midpart=midpart+'","items":["Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute"]'
            midpart=midpart+'}]'
        if(self.knotentyp=="LogicNode"):
            midpart='["Gatter",{"selected":"'
            midpart=midpart+self.functionName
            midpart=midpart+'","items":["AND","OR","XOR","NAND","NOR","XNOR"]'
            midpart=midpart+'}]'
        if(self.knotentyp=="BooleanNode"):
            midpart='["Operation",{"selected":"'
            if(self.functionName=="Equals"):
                midpart=midpart+'=='
            elif(self.functionName=='Greater'):
                midpart=midpart+'>'
            elif(self.functionName=='Smaller'):
                midpart=midpart+'<'
            elif(self.functionName=='GreaterThan'):
                midpart=midpart+'>='
            elif(self.functionName=='SmallerThan'):
                midpart=midpart+'<='
            midpart=midpart+'","items":["==",">","<",">=","<="]'
            midpart=midpart+'}]'
        options = options+midpart +'],'
        return options
        #if (self.knotentyp =="MathNode"):
        #    mathnodeList = ["Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute"]
        #    print('Mathnode')
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
        self.functionName = functionName #Name im Stil von Add, Substract
        self.parameterList=list()
        self.knotentyp=knotentyp #Mathnode, use
        self.output  = None
        self.nodeList = list()
        self.manager = manager
        self.fid = 0
