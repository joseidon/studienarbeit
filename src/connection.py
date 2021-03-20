class connection:
    start = "hello"
    end = "world"
    id = 0

    def getDict(self):
        cDict = {
            "id": self.id,
            "from": self.start,
            "to": self.end
        }
        return cDict

    def __init__(self,id,start,end):
        self.id = id
        self.start = start
        self.end = end

