import managermanager as mm
import funktionsmanager as fm
import functioninstance as fi


def main():
    manager= fm.funktionsmanager()
    while(1==1):
        readLine(manager)

def readLine(manager):
    text= input("prompt")

    #vManager = manager.getVariablenManager()
    decideInputType(text, manager)
    #vManager.getDict()
    
    #inputt = text.replace(' ','')
    #print(inputt)
    #inputList = inputt.split("=")
    #name = inputList[0]
    #isconstant = name.startswith("$") or name.startswith("%") or name.startswith("!")
    #if isconstant:
    #    createConstant()
    #print(inputList[1])
    #fManager = manager.getFunctionManager
    #fManager.getFunktionFromString(inputList[1])

def getManager(self):
        return self.manager

def decideInputType(text, manager):
    if text.startswith('node'):
        createNode(text, manager)
    elif text.startswith('printjson'):
        getDict(manager)
    elif text.startswith('exit'):
        exit()     
    else:    
        print("Wrong input, either start with 'node', 'printjson' or 'exit'")

def createNode(text,manager):
    manager.createNode(text)
        
           

def getDict(manager):
    headDict = '{"nodes": ['
    fDict = manager.getDict(headDict)
    fDict=fDict+'"panning": {"x": 0,"y": 0},"scaling": 1,"mlsettings": {"batchCount": 100,"workerCount": 4,"csvDelimiter": ";"} }'
    #add connections
    #fDict=fDict+']}'
    with open('data.json', 'w') as outfile:
        print(fDict)
            #json.dump(fDict, outfile)
        outfile.write(fDict)

            
def checkForBrackets(self, text):
    varFunctionInstance = None
    if "(" in text:
        fManager = self.manager.getFunctionManager()
        varFunctionInstance = fManager.getFunktionFromString(text)
    else:
            #hier Konstante einfügen
            #fManager.
        print("Constant")
        kManager = self.manager.getKonstantenManager()
        varFunctionInstance = kManager.createNamedKonstante(text)

        return varFunctionInstance

    



if __name__ == '__main__':
    main()