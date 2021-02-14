

def main():
    print ("test")
    while 1==1:
        einlesen()

def einlesen():
    text= input("prompt")
    print(text)
    if text.startswith("knoten"):
        knotenString = text.replace('knoten ', '')
        newString = knotenString.replace(' ','')
        #print(knotenString)
        knotenCreation(newString)
    elif  text.startswith("var"):
        varString = text.replace('var ', '')
        newString = varString.replace(' ','')
        #print(varString)
        varCreation(varString)
    else:
        print("Wrong Input")

def varCreation(input):
    print("new var")
    print(input)

def knotenCreation(input):
    print("new node")
    print(input)
    inputList = input.split("=")
    print(inputList[0])
    print(inputList[1])




if __name__ == '__main__':
    main()