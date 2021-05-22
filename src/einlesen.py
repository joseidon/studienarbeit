import managermanager as mm
import variablenmanager as vm
import funktionsmanager as fm
import konstantenManager as km

def main():
    manager=mm.managermanager()
    vManager=vm.variablenManager(manager)
    manager.setVariablenManager(vManager)
    fManager = fm.funktionsmanager(manager)
    manager.setFunctionManager(fManager)
    kManager = km.konstantenManager(manager)
    manager.setKonstantenManager(kManager)
    while(1==1):
        readLine(manager)

def readLine(manager):
    text= input("prompt")

    vManager = manager.getVariablenManager()
    vManager.readLine(text)
    vManager.getDict()
    
    #inputt = text.replace(' ','')
    #print(inputt)
    #inputList = inputt.split("=")
    #name = inputList[0]
    #isconstant = name.startswith("$") or name.startswith("%") or name.startswith("!")
    #if isconstant:
    #    createConstant()
    #print(inputList[1])
    #fManager = manager.getFunctionManager
    #fManager.getFunktionFromString(inputList[1])



if __name__ == '__main__':
    main()