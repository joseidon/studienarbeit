import parameterinstance as pi
import funktionsmanager as fm
import connection as cn
class parameter:
    pid=0
    def createParameterInstance(self, value, manager):
        if (value.startswith('*')):
            value=value[1:]
            con=''
            if(manager.checkName(value)):
                con=value+"out"
                c=cn.connection(con,'ni_'+self.name + str(parameter.pid))
                manager.addConnection(c)
            value=0
            p = pi.parameterinstance(self,'ni_'+ self.name + str(parameter.pid), value)
            parameter.pid=parameter.pid+1
            return p
        else:
            p = pi.parameterinstance(self, 'ni_'+self.name + str(parameter.pid), value)
            parameter.pid=parameter.pid+1
        #print(self.pid)
            return p

    def createOuput(self, name, manager):
        #print("Output")
        oName = name + "out"
        p = pi.parameterinstance(self, oName, None)
        return p

    def getName(self):
        return self.name

    def getTyp(self):
        return self.typ

    def setFunction(self, f):
        self.function=f

    def setCustom(self):
        self.customflag=True

    def __init__(self, name, typ):
        self.name=name
        self.typ=typ
        self.customflag=False
            