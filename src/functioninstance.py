import funktion

class functioninstance:
    id=1
    position=0
    
    def addParameterInstance(self, p):
        self.parameterList.append(p)

    def setLabel(self, label):
        self.label=label
    
    def setOutput(self, output):
        #self.output = output
        self.parameterList.append(output)
    
    def getFunktion(self):
        return self.function
        
    def getLabel(self):
        return self.label

    def getInterfaces(self):
        interfaces='"state": { },"interfaces": ['
        first=True
        
        for p in self.parameterList:
            if (first!= True):
                interfaces=interfaces+','     
            first=False
            interfaces=interfaces+p.getDict()
        interfaces=interfaces+'],'
            #interfaces=interfaces + '["Value 1",{"id":"' +self.function.functionName + str(self.fid) +'v1","value": 0}],'
            #interfaces=interfaces + '["Value 2",{"id":"' +self.function.functionName + str(self.fid) +'v2","value": 0}],'
            #interfaces=interfaces + '["Result",{"id":"' +self.function.functionName + str(self.fid) +'r","value": null}]],'
        return interfaces
   

    def getDict(self):
        dictHead='{'
        dictH = '"type":"{}","id": "node_{}","name":"{}",'.format(self.function.getKnotenTyp(),self.fid,self.function.getKnotenTyp(),self.fid)
        dictHead= dictHead+dictH
        options = self.function.getOption(self)
        interfaces = self.getInterfaces()
        #dictend =  '"position": {"x": '+str(self.pos)+',"y": '+str(self.pos)+' }, "width": 200, "twoColumn": false}'
        print(dictHead)
        print(options)
        print(interfaces)
        
        dictend =  '"position": {"x": '+str(self.pos)+',"y": '+str(self.pos)+' }, "width": 200, "twoColumn": false}'
        print(dictend)
        dictHead=dictHead+options+interfaces+dictend
        return dictHead

    def __init__(self, function, fid, name):
        self.pos= functioninstance.position
        self.function = function
        self.parameterList = list()
        self.fid = functioninstance.id
        self.label = None
        functioninstance.id=functioninstance.id+1
        functioninstance.position=functioninstance.position+200
