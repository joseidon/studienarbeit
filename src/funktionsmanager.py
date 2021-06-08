import funktion
import parameter
import connection

class funktionsmanager:
    
    def getDict(self, headDict):
        first=True
        stringList=[]
        for f in self.funktionsList.items():
            #hier zusammenfügen
            dictList = f[1].getDict(first)
            if(dictList!=''):
                first=False
            #for d in dictList:
                #if(first!=True):
                    #headDict=headDict+ ','
            #    first=False
                #hier zusammenfügen
            headDict=headDict+ dictList
        
        headDict= headDict + '],"connections": ['
        first=True
        for c in self.connectionList:
            if(first!=True):
                headDict=headDict+ ','
            first=False
            headDict = headDict + c.getDict()
        headDict = headDict+'],'
        return headDict

    def addConnection(self, c):
        self.connectionList.append(c)

    def checkName(self, newName):
        if newName in self.nameList:
            return True
        else:
            return False



    def createNode(self,text):
        text=text[4:]
        text = text.replace(" ", "")      
        information = text.split("=")
        name=information[0]
        if name in self.nameList:
            print("Error: No unique node name")
            return
        inputList = information[1].split('(')
        typ = inputList[0]

        arguements = inputList[1].split(')')
        f = self.funktionsList[typ]
        if f is None:
            print("ungültiger Knotentyp: ", typ)
            return
        f.createFunctionInstance(name,arguements[0], self)
        self.nameList.append(name)

        return
 


    def getFunktionFromString(self, eingabe):
        text = eingabe.replace(' ','')
        inputList = text.split('(')
        typ = inputList[0]
        arguements = inputList[1].split(')')

        f = self.funktionsList[typ]
        if f is None:
            print("ungültiger Knotentyp: ", typ)
            return
        return f.createFunctionInstance(arguements[0])


    def __init__(self):
        self.funktionsList={}
        self.nameList=[]
        self.connectionList=[]

        print("funktionsmanager created")

        mathnodes=["Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute"]
        for a in mathnodes:
            add=funktion.funktion(a, "MathNode", self)
            addp1=parameter.parameter("Value 1", "Number")
            addp2=parameter.parameter("Value 2", "Number")
            addOut=parameter.parameter("Result", "Number")
            add.parameterList.append(addp1)
            add.parameterList.append(addp2)
            add.setOutput(addOut)
            self.funktionsList[add.getName()] = add

        
        
        output=funktion.funktion("Output", "OutputNode", self)
        outputp1=parameter.parameter("Input", "Number")
        output.parameterList.append(outputp1)
        self.funktionsList[output.getName()] = output

        uniform=funktion.funktion("Uniform", "UniformNode", self)
        uni1=parameter.parameter("Seed", "Number")
        uni2=parameter.parameter("Min", "Number")
        uni3=parameter.parameter("Max", "Number")
        uni4=parameter.parameter("Discrete", "Boolean")      
        uniout=parameter.parameter("Output", "Number")
        uniform.parameterList.append(uni1)
        uniform.parameterList.append(uni2)
        uniform.parameterList.append(uni3)
        uniform.parameterList.append(uni4)
        uniform.setOutput(uniout)
        self.funktionsList[uniform.getName()] = uniform

        normal=funktion.funktion("Normal", "NormalNode", self)
        nor1=parameter.parameter("Seed", "Number")
        nor2=parameter.parameter("Mean", "Number")
        nor3=parameter.parameter("Std. Dev.", "Number")
        nor4=parameter.parameter("Discrete", "Boolean")      
        norout=parameter.parameter("Output", "Number")
        normal.parameterList.append(nor1)
        normal.parameterList.append(nor2)
        normal.parameterList.append(nor3)
        normal.parameterList.append(nor4)
        normal.setOutput(norout)
        self.funktionsList[normal.getName()] = normal

        exponential=funktion.funktion("Exponential", "ExponentialNode", self)
        exp1=parameter.parameter("Seed", "Number")
        exp2=parameter.parameter("Lambda", "Number")
        exp3=parameter.parameter("Discrete", "Boolean")
        expout=parameter.parameter("Output", "Number")
        exponential.parameterList.append(exp1)
        exponential.parameterList.append(exp2)
        exponential.parameterList.append(exp3)
        exponential.setOutput(expout)
        self.funktionsList[exponential.getName()] = exponential

        percentage=funktion.funktion("Percentage", "PercentageNode", self)
        per1=parameter.parameter("Value", "Number")
        per1=parameter.parameter("Seed", "Number")
        per1=parameter.parameter("Percentage", "Number")
        per1=parameter.parameter("Discrete", "Boolean")      
        perout=parameter.parameter("Output", "Number")
        percentage.parameterList.append(per1)
        percentage.parameterList.append(per1)
        percentage.parameterList.append(per1)
        percentage.parameterList.append(per1)
        percentage.setOutput(perout)
        self.funktionsList[percentage.getName()] = percentage

        logicnodes=["AND","OR","XOR","NAND","NOR","XNOR"]
        for a in logicnodes:
            add=funktion.funktion(a, "LogicNode", self)
            addp1=parameter.parameter("A", "Boolean")
            addp2=parameter.parameter("B", "Boolean")
            addOut=parameter.parameter("Result", "Boolean")
            add.parameterList.append(addp1)
            add.parameterList.append(addp2)
            add.setOutput(addOut)
            self.funktionsList[add.getName()] = add

        logicnodes=["Equals","Greater","Smaller","GreaterThan","SmallerThan"]
        for i in logicnodes:
            add=funktion.funktion(i, "BooleanNode", self)
            addp1=parameter.parameter("Value 1", "Number")
            addp2=parameter.parameter("Value 2", "Number")
            addp3=parameter.parameter("Round Values", "Boolean")
            addp4=parameter.parameter("Invert Output", "Boolean")
            addOut=parameter.parameter("Result", "Boolean")
            add.parameterList.append(addp1)
            add.parameterList.append(addp2)
            add.parameterList.append(addp3)
            add.parameterList.append(addp4)
            add.setOutput(addOut)
            self.funktionsList[add.getName()] = add
            