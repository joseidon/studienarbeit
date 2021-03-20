import konstante
import connection

class konstantenManager:
    konstantenList = list()
    ConnectionList = list()
    connectionID = 1

    def addKonstante(self, konstante,typ):
        #change konstante to konstante
        k = konstante(konstante,typ)
        self.konstantenList.append(k)
        return k

    def getOrCreateKonstante(self, konstante, typ):
        for k in self.konstantenList:
            if konstante == k.getName():                
                return k
        k=self.addKonstante(konstante, typ)
        return k
        
    def createConnection(self, start, end):
        

        c = connection.connection(self.connectionID,start,end)
        self.connectionID = self.connectionID + 1
        self.ConnectionList.append(c)
    
    def getCList(self):
        return self.ConnectionList
        

    def __init__(self):
        print("create List")