class connection:
    idcnt=0

    def getDict(self):
        cdict='{"id": "'+str(self.id)+'","from": "'+str(self.start)+'", "to": "'+str(self.end)+'"}'
        return cdict

    def __init__(self,start,end):
        self.id = connection.idcnt
        self.start = start
        self.end = end
        connection.idcnt=connection.idcnt+1

