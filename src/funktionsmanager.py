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
        per2=parameter.parameter("Seed", "Number")
        per3=parameter.parameter("Percentage", "Number")
        per4=parameter.parameter("Discrete", "Boolean")      
        perout=parameter.parameter("Output", "Number")
        percentage.parameterList.append(per1)
        percentage.parameterList.append(per2)
        percentage.parameterList.append(per3)
        percentage.parameterList.append(per4)
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

        index=funktion.funktion("Index", "IndexValueNode", self)
        indout=parameter.parameter("Output", "Number")
        index.setOutput(indout)
        self.funktionsList[index.getName()] = index

        custom=funktion.funktion("Custom", "CustomNode", self)
        cus1=parameter.parameter("Seed", "String")
        cus2=parameter.parameter("Min", "Number")
        cus3=parameter.parameter("Max", "Number")
        cus4=parameter.parameter("Discrete", "Boolean")      
        cusout=parameter.parameter("Output", "Number")
        custom.parameterList.append(cus1)
        custom.parameterList.append(cus2)
        custom.parameterList.append(cus3)
        custom.parameterList.append(cus4)
        custom.setOutput(cusout)
        self.funktionsList[custom.getName()] = custom

        discrete=funktion.funktion("Discrete", "DiscreteNode", self)
        dis1=parameter.parameter("Seed", "String")
        dis2=parameter.parameter("Min", "Number")
        dis3=parameter.parameter("Max", "Number")
        disout=parameter.parameter("Output", "Number")
        discrete.parameterList.append(dis1)
        discrete.parameterList.append(dis2)
        discrete.parameterList.append(dis3)
        discrete.setOutput(disout)
        self.funktionsList[discrete.getName()] = discrete

        ifnode=funktion.funktion("If", "IfNode", self)
        if1=parameter.parameter("Condition", "Boolean")
        if2=parameter.parameter("True Value", "Boolean")
        if3=parameter.parameter("False Value", "Boolean")
        ifout=parameter.parameter("Output", "Boolean")
        ifnode.parameterList.append(if1)
        ifnode.parameterList.append(if2)
        ifnode.parameterList.append(if3)
        ifnode.setOutput(ifout)
        self.funktionsList[ifnode.getName()] = ifnode

        switch=funktion.funktion("Switch", "SwitchNode", self)
        sw1=parameter.parameter("Switch", "Boolean")
        sw2=parameter.parameter("Value 1", "Boolean")
        sw3=parameter.parameter("Value 2", "Boolean")
        swout=parameter.parameter("Output", "Boolean")
        sw2.setCustom()
        sw3.setCustom()
        switch.parameterList.append(sw1)
        switch.parameterList.append(sw2)
        switch.parameterList.append(sw3)
        switch.setOutput(swout)
        self.funktionsList[switch.getName()] = switch

        func=funktion.funktion("Function", "FunctionNode", self)
        f1=parameter.parameter("input", "Boolean")
        f1.setCustom()
        fout=parameter.parameter("output", "Boolean")
        func.parameterList.append(f1)
        func.setOutput(fout)
        self.funktionsList[func.getName()] = func

        con=funktion.funktion("Constraint", "ConstraintNode", self)
        con1=parameter.parameter("Is Valid", "Boolean")
        con.parameterList.append(con1)
        self.funktionsList[con.getName()] = con

        stringl=funktion.funktion("StringList", "StringListNode", self)
        s1=parameter.parameter("Index", "Number")
        sout=parameter.parameter("String", "String")
        stringl.parameterList.append(s1)
        stringl.setOutput(sout)
        self.funktionsList[stringl.getName()] = stringl




        


