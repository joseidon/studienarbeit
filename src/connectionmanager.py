import connection
class connectionmanager:

    def getDict(self):
        cons =""
        for c in self.connectionList:
            cons = cons + c.getDict()
        return cons

    def addConnection(self,conn):
        self.conncetionList.append(conn)

    def init(self):
        self.connectionList=[]