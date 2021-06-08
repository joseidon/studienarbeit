import variable as var
import funktionsmanager as fm
import managermanager as mm
import functioninstance as fi
import json

class variablenManager:

    #def addVar(self, newVar):
    #    self.varList[newVar]=var.variable(newVar, self)

    def getManager(self):
        return self.manager

    def readLine(self, text):
        if text.startswith('node'):
            self.createNode(text)
        elif text.startswith('printjson'):
            self.getDict()
        elif text.startswith('exit'):
            exit()     
        else:    
            print("Wrong input, either start with 'node', 'printjson' or 'exit'")

    def createNode(self,text):
        fManager = self.manager.getFunctionManager()
        fManager.createNode(text)
        

    def checkForEqual(self, text):
        text = text.replace(" ", "")
        varObject = None
        if "=" in text:
            textList = text.split("=")
            print(self.varList)
            varObject = self.checkForBrackets(textList[1])
            print(textList)
            if self.varList[textList[0]] is not None:
                self.varList[textList[0]].setValue(varObject)
            else:
                v = var.variable(textList[0],varObject.getOutputTyp(),self)
                v.setValue(varObject)
                self.varList[textList[0]] = v
                #create Variable
                #v = var.variable(,varObject.,self)
                print("create variable")
        else:
            print("Ungültige Eingabe")
            

    def getDict(self):
        fManager = self.manager.getFunctionManager()
        headDict = '{"nodes": [{'

        fDict = fManager.getDict(headDict)
        fDict = fDict + '],"connections": ['
        #add connections
        fDict=fDict+']}'
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

    
    def __init__(self, manager):
        self.varList = {}
        self.manager = manager