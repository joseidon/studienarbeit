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

if __name__ == '__main__':
    main()