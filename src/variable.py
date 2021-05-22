class variable:

    def setValue(self, value):
        self.value = value

    def getTyp(self):
        return self.typ

    def getValue(self):
        return self.value



    def __init__(self, name, typ, manager):
        self.name = name
        self.typ = typ
        self.value = None
        self.manager = manager