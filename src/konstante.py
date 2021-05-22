class konstante:


    def getDict(self):
        posDict = {
                "x": 0,
                "y" : 0
            }
        kDict = {
            "type" : self.typ, 
            "id" : self.name,
            "name" : self.name,
            "options" : [],
            "state" : {},
            "interfaces":[],
            "position" : posDict,
            "width" : 200,
            "twoColumn": False
        }
        outputID = self.name + "out"
        outputValueDict = {
            "id": outputID,
            "value": "null"
        }
        outputDict = {
            "Output":outputValueDict
        }

        optionDict = {
            "Value" : self.name
        }
        kDict["options"].append(optionDict)
        

        kDict["interfaces"].append(outputDict)

        return kDict

    def getName (self):
        return self.name

    def getOutputID (self):
        outputID = self.name + "out"
        return outputID

    def __init__(self,name,typ, value, kManager):
        types = ["Number","String","Boolean"]
        print("Konstante")
        self.name=name
        self.value=value
        self.kManager=kManager
        if typ in types:
            self.typ = typ #typen regeln
        else:
            print("Kein gültiger Typ")
