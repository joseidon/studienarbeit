

def main():
    print ("test")
    while 1==1:
        einlesen()

def einlesen():
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
    knotenCreation(name, typ, options)

def knotenCreation(name, typ, options):
    nodeTypes = "uniform","normal","exponential","custom","discrete","percentage","if","switch","function","AND","OR","XOR","NAND","NOR","XNOR","==",">","<",">=","<=","constraint","Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute","stringlist","output" 
    if typ not in nodeTypes:
        print("Error: no type")
        return
    
    


def createConstant():
    print("Konstante")




if __name__ == '__main__':
    main()