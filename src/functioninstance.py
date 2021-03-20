import konstantenManager as km

class functioninstance:
    name = "foo"
    typ = "bar"
    parameterList = list()
    option=list()
    knoten = "Hello"
    fid = "World"
    #interfaceList
    #parameters

    def addParameter(self, parameter, option):
        self.parameterList.append(parameter)
        self.option=option


    def getDict(self):
        posDict = {
                "x": 0,
                "y" : 0
            }
        fDict = {
            "type" : self.knoten,
            "id" : self.fid,
            "name" : self.name,
            "options" : [],
            "state" : {},
            "interfaces":[],
            "position" : posDict,
            "width" : 200,
            "twoColumn": False
        }
        outputID = self.fid + "out"
        outputValueDict = {
            "id": outputID,
            "value": "null"
        }
        outputDict = {
            "Output":outputValueDict
        }
        

        fDict["interfaces"].append(outputDict)
        for p in self.parameterList:
            fDict["interfaces"].append(p.getDict())
        return fDict


    def print(self):
        print("Function:")
        print("Name: ", self.name)
        print("Typ: ", self.typ)
        print("Knoten: ", self.knoten)
        for p in self.parameterList:
            p.print()
    


    def __init__(self,name,typ,knotentyp):
        self.name = name
        self.typ = typ
        self.knoten = knotentyp
        self.fid = name
    