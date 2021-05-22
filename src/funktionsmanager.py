import funktion
import parameter

class funktionsmanager:
    
    def getDict(self, headDict):
        for f in self.funktionsList.items():
            dictList = f[1].getDict()
            for d in dictList:
                headDict["nodes"].append(d)
        return headDict

    def addKnoten(self):
        print("addKnoten")

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


    def __init__(self, manager):
        self.manager = manager
        self.funktionsList={}

        print("funktionsmanager created")
        add=funktion.funktion("Add", "MathNode", self)
        addp1=parameter.parameter("Value1", "Number")
        addp2=parameter.parameter("Value2", "Number")
        addOut=parameter.parameter("Result", "Number")
        add.parameterList.append(addp1)
        add.parameterList.append(addp2)
        add.setOutput(addOut)
        self.funktionsList[add.getName()] = add

        sub=funktion.funktion("Subtract", "MathNode", self)
        subp1=parameter.parameter("Value1", "Number")
        subp2=parameter.parameter("Value2", "Number")
        subOut=parameter.parameter("Result", "Number")
        sub.parameterList.append(subp1)
        sub.parameterList.append(subp2)
        sub.setOutput(subOut)
        self.funktionsList[sub.getName()] = sub

        mul=funktion.funktion("Multiply", "MathNode", self)
        mulp1=parameter.parameter("Value1", "Number")
        mulp2=parameter.parameter("Value2", "Number")
        mulOut=parameter.parameter("Result", "Number")
        mul.parameterList.append(mulp1)
        mul.parameterList.append(mulp2)
        mul.setOutput(mulOut)
        self.funktionsList[mul.getName()] = mul

        div=funktion.funktion("Divide", "MathNode", self)
        divp1=parameter.parameter("Value1", "Number")
        divp2=parameter.parameter("Value2", "Number")
        divOut=parameter.parameter("Result", "Number")
        div.parameterList.append(divp1)
        div.parameterList.append(divp2)
        div.setOutput(divOut)
        self.funktionsList[div.getName()] = div

        sine=funktion.funktion("Sine", "MathNode", self)
        sinep1=parameter.parameter("Value1", "Number")
        sinep2=parameter.parameter("Value2", "Number")
        sineOut=parameter.parameter("Result", "Number")
        sine.parameterList.append(sinep1)
        sine.parameterList.append(sinep2)
        sine.setOutput(sineOut)
        self.funktionsList[sine.getName()] = sine

        cos=funktion.funktion("Cosine", "MathNode", self)
        cosp1=parameter.parameter("Value1", "Number")
        cosp2=parameter.parameter("Value2", "Number")
        cosOut=parameter.parameter("Result", "Number")
        cos.parameterList.append(cosp1)
        cos.parameterList.append(cosp2)
        cos.setOutput(cosOut)
        self.funktionsList[cos.getName()] = cos

        tan=funktion.funktion("Tangent", "MathNode", self)
        tanp1=parameter.parameter("Value1", "Number")
        tanp2=parameter.parameter("Value2", "Number")
        tanOut=parameter.parameter("Result", "Number")
        tan.parameterList.append(tanp1)
        tan.parameterList.append(tanp2)
        tan.setOutput(tanOut)
        self.funktionsList[tan.getName()] = tan

        arcs=funktion.funktion("Arcsine", "MathNode", self)
        arcsp1=parameter.parameter("Value1", "Number")
        arcsp2=parameter.parameter("Value2", "Number")
        arcsOut=parameter.parameter("Result", "Number")
        arcs.parameterList.append(arcsp1)
        arcs.parameterList.append(arcsp2)
        arcs.setOutput(arcsOut)
        self.funktionsList[arcs.getName()] = arcs

        arcc=funktion.funktion("Arccosine", "MathNode", self)
        arccp1=parameter.parameter("Value1", "Number")
        arccp2=parameter.parameter("Value2", "Number")
        arccOut=parameter.parameter("Result", "Number")
        arcc.parameterList.append(arccp1)
        arcc.parameterList.append(arccp2)
        arcc.setOutput(arccOut)
        self.funktionsList[arcc.getName()] = arcc

        arct=funktion.funktion("Arctangent", "MathNode", self)
        arctp1=parameter.parameter("Value1", "Number")
        arctp2=parameter.parameter("Value2", "Number")
        arctOut=parameter.parameter("Result", "Number")
        arct.parameterList.append(arctp1)
        arct.parameterList.append(arctp2)
        arct.setOutput(arctOut)
        self.funktionsList[arct.getName()] = arct

        power=funktion.funktion("Power", "MathNode", self)
        powerp1=parameter.parameter("Value1", "Number")
        powerp2=parameter.parameter("Value2", "Number")
        powerOut=parameter.parameter("Result", "Number")
        power.parameterList.append(powerp1)
        power.parameterList.append(powerp2)
        power.setOutput(powerOut)
        self.funktionsList[power.getName()] = power

        loga=funktion.funktion("Logarithm", "MathNode", self)
        logap1=parameter.parameter("Value1", "Number")
        logap2=parameter.parameter("Value2", "Number")
        logaOut=parameter.parameter("Result", "Number")
        loga.parameterList.append(logap1)
        loga.parameterList.append(logap2)
        loga.setOutput(logaOut)
        self.funktionsList[loga.getName()] = loga

        minimum=funktion.funktion("Minimum", "MathNode", self)
        minimump1=parameter.parameter("Value1", "Number")
        minimump2=parameter.parameter("Value2", "Number")
        minimumOut=parameter.parameter("Result", "Number")
        minimum.parameterList.append(minimump1)
        minimum.parameterList.append(minimump2)
        minimum.setOutput(minimumOut)
        self.funktionsList[minimum.getName()] = minimum

        maximum=funktion.funktion("Maximum", "MathNode", self)
        maximump1=parameter.parameter("Value1", "Number")
        maximump2=parameter.parameter("Value2", "Number")
        maximumOut=parameter.parameter("Result", "Number")
        maximum.parameterList.append(maximump1)
        maximum.parameterList.append(maximump2)
        maximum.setOutput(maximumOut)
        self.funktionsList[maximum.getName()] = maximum

        rou=funktion.funktion("Round", "MathNode", self)
        roup1=parameter.parameter("Value1", "Number")
        roup2=parameter.parameter("Value2", "Number")
        rouOut=parameter.parameter("Result", "Number")
        rou.parameterList.append(roup1)
        rou.parameterList.append(roup2)
        rou.setOutput(rouOut)
        self.funktionsList[rou.getName()] = rou

        mod=funktion.funktion("Modulo", "MathNode", self)
        modp1=parameter.parameter("Value1", "Number")
        modp2=parameter.parameter("Value2", "Number")
        modOut=parameter.parameter("Result", "Number")
        mod.parameterList.append(modp1)
        mod.parameterList.append(modp2)
        mod.setOutput(modOut)
        self.funktionsList[mod.getName()] = mod

        absolute=funktion.funktion("Absolute", "MathNode", self)
        absolutep1=parameter.parameter("Value1", "Number")
        absolutep2=parameter.parameter("Value2", "Number")
        absoluteOut=parameter.parameter("Result", "Number")
        absolute.parameterList.append(absolutep1)
        absolute.parameterList.append(absolutep2)
        absolute.setOutput(absoluteOut)
        self.funktionsList[absolute.getName()] = absolute
        

