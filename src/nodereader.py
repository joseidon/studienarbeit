import konstante
import pandas
import parameter
import functioninstance as fi
import numpy as np
import jsonwriter as jw
import konstantenManager as km

def main():
    print ("test")
    functionInstanceList = list()
    kManager = km.konstantenManager()
    while 1==1:
        einlesen(functionInstanceList, kManager)
       

def printAll(functionInstanceList):
    print("print everything")
    for functionF in functionInstanceList:
        functionF.print()

#eingabe name=typ(option,option)
def einlesen(functionInstanceList, kManager):
    
    text= input("prompt")
    inputt = text.replace(' ','')
    print(inputt)
    inputList = inputt.split("=")
    name = inputList[0]
    isconstant = name.startswith("$") or name.startswith("%") or name.startswith("!")
    if isconstant:
        createConstant()
    print(inputList[1])
    stringList = inputList[1].split('(')
    typ = stringList[0]
    options = stringList[1]
    knotenCreation(name, typ, options, functionInstanceList, kManager)
    printAll(functionInstanceList)

def knotenCreation(name, nodetyp, options, fiList, kManager):
    nodeTypes = "uniform","normal","exponential","custom","discrete","percentage","if","switch","function","AND","OR","XOR","NAND","NOR","XNOR","==",">","<",">=","<=","constraint","Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute","stringlist","output" 
    if nodetyp not in nodeTypes:
        print("Error: no type")
        return
    #options zerstückeln
    optionList = options.split(",")
    df = pandas.read_csv("knotenlist.csv")
    functionTypeParameters = df[nodetyp]
    knotentyp = functionTypeParameters['Knoten']

    newFunction = fi.functioninstance(name,nodetyp, knotentyp)
    fiList.append(newFunction)
    

    anzPara = functionTypeParameters['anzPara']
    anzPara = np.int_(anzPara)
    
    for x in range(anzPara):
        print(np.int_(functionTypeParameters[x+2]))
        p = parameter.parameter(np.int_(functionTypeParameters[x+2]), name, kManager,optionList[x])
        newFunction.addParameter(p,optionList[x])
    print(functionTypeParameters)

    print("create function Instance")
    jw.printToJSON(fiList)
    
    

def createConstant():
    print("Konstante")


if __name__ == '__main__':
    main()