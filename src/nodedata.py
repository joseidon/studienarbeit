class notedata:
    nodetypes=dict()

    

    def addMath(self):
        math = {
            "items": [
                        "Add",
                        "Subtract",
                        "Multiply",
                        "Divide",
                        "Sine",
                        "Cosine",
                        "Tangent",
                        "Arcsine",
                        "Arccosine",
                        "Arctangent",
                        "Power",
                        "Logarithm",
                        "Minimum",
                        "Maximum",
                        "Round",
                        "Modulo",
                        "Absolute"
            ], 

            
            "interface1": ["Value 1","Number"],
            "interface2": ["Value 2","Number"]
                   
            
            }
        self.nodetypes["Add"] = math
        return math

    def get(self, type):
        self.addMath()
        result = self.nodetypes[type]
        return result

    def __init__(self):
        print("init")
