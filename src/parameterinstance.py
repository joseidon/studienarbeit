class parameterinstance:

    def setValue(self, value):
        self.value = value
        if(self.value==None):
            self.value="null"
        #print(self.value)

    def getValue(self):
        return self.value

    def getParamter(self):
        return self.parameter

    def getDict(self):
        if(self.parameter.name=='Input'):
            interface='["' + self.parameter.name + '",{"id":"' +str(self.pid) +'"}]'
            #print('world')
            #print(interface)
            return interface
        
        interface='["' + self.parameter.name + '",{"id":"' +str(self.pid) +'","value": ' +str(self.value).lower()+'}]'

        return interface


    def __init__(self, parameter, pid, value):
        self.pid = pid
        self.parameter = parameter
        self.value = value
        if(self.value==None):
            self.value="null"
        print(pid)
        print(value)