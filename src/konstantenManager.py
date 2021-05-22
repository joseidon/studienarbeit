import konstante
import managermanager

class konstantenManager:
    

    def addKonstante(self, konstante, typ):
        #change konstante to konstante
        k = konstante.konstante(konstante,typ, konstante)
        self.konstantenList[k] = k
        return k

    def getOrCreateKonstante(self, konstante, typ):
        #rework
        for k in self.konstantenList:
            if konstante == k.getName():                
                return k
        k=self.addKonstante(konstante, typ)
        return k
        
    #outdated

    def createNamedKonstante(self, name, typ, konstante):
        k = konstante.konstante(name, typ, konstante)
        return k
        print("test")


    def __init__(self, manager):
        self.manager = manager
        self.konstantenList = {}
        print("create List")