import pandas as pd
import numpy as np
import konstantenManager as km

class parameter:
    name = None
    typ = None
    #knoten = "placeholder"
    pid = 1
    #inputValue 

    def print(self):
        print("Parameterame: ", self.name)
        print("Typ: ", self.typ)
        #print("Knoten: ", self.knoten)
        print("ID: ", self.pid)

    def getDict(self):
        
        paramDict = {
            "id" : self.pid,
            "value" : "null"
        }
        pDict = {
            self.name : paramDict
        }

        return pDict
#
    def __init__(self, knid, knotenname, kManager, option):
        parameterList = pd.read_csv("parameterList.csv")
        print(parameterList)
        df = parameterList[str(knid)]
        print("ParamterCreation: ", df['name'])
        self.pid = knotenname+"input"+str(df['name'])
        self.name=df['name']
        self.typ = df['type']

        #create Connection