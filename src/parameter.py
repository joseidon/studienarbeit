import pandas 

class parameter:
    #name 
    #typ
    #id
    #inputValue

#pID, fName, inputValue
    def __init__(self):
        df = pandas.read_json(parameterList.json)
        #self.id = name + fName
        print("create parameter")