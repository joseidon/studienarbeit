{
    type
    id
    name
    options:[  #unterschied zwischen den Knoten
        [
            
        ]
    ]
    state
    interfaces:[
        [
            "Output"
            {
                id
                value
            }
        ]
    ]
    position{
        x
        y
    }
    width
    twocolumn
}


(Knoten + Verbindung)(Knotenname)=(Knotentyp)(option)* 



Knoten valueOne = NumberValue(0.02)
Knoten valueTwo = NumberValue(0.02)
Knoten addOneTwo = add(valueOne,valueTwo)
var i = addOneTwo
Knoten outputOne = Output("Ergebnis", i) 

formel i=a+b+c



"uniform","normal","exponential","custom","discrete","percentage","if","switch","function","AND","OR","XOR","NAND","NOR","XNOR","==",">","<",">=","<=","constraint","Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute","stringlist","output"
