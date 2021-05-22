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
        if text.startswith('var'):
            self.checkVarValid(text)
        elif text.startswith('printjson'):
            self.getDict()
        elif text.startswith('exit'):
            exit()     
        else:    
            self.checkForEqual(text)

    def checkVarValid(self, text):
        types = ["Number", "Boolean", "String"]
        varText = text.split(' ')
        if len(varText) !=3:
            print("wrong number of arguements for Variable creation. Pease type var [typ] [name]")
            return
        varTyp = varText[1]
        if varTyp not in types:
            print("ungültiger Variablentyp: ", varTyp)
            return
        varName = varText[2]
        v = var.variable(varName, varTyp, self)
        self.varList[varName] = v

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
        headDict = {
            "nodes":[]
        }
        fDict = fManager.getDict(headDict)

        with open('data.json', 'w') as outfile:
            print(fDict)
            json.dump(fDict, outfile)
        

    def typeCheck(self, v, varObject):
        if varObject.getOutputTyp()==v.getTyp:
            return
        else:
            print("Typen nicht konform")
            #knoten löschen

            
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