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


gcloud compute --project=hadooptest-304213 instances create big-data --zone=europe-west3-c --machine-type=n1-highmem-4 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --image=ubuntu-2004-focal-v20210129 --image-project=ubuntu-os-cloud --boot-disk-size=40GB --boot-disk-type=pd-standard --boot-disk-device-name=big-data