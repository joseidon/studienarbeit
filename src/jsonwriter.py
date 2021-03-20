import json

def main():
    data = {}
    data['nodes'] = []
    #data['people'].append({
    #'name': 'Scott',
    #'website': 'stackabuse.com',
    #'from': 'Nebraska'
    #})
    print("main")
    addNode(data)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def addNode(data):
    data['nodes'].append({
        'type': '1',
        'id': '1',
        'name': 'name'
    })

def printToJSON(functionInstanceList):
    headDict = {
        "nodes":[]
    }
    for f in functionInstanceList:
        newDict = f.getDict()
        headDict["nodes"].append(newDict)

    with open('data.json', 'w') as outfile:
        json.dump(headDict, outfile)