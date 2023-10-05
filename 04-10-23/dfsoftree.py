def preorder(root,graph,vistedplaces):
    if root not in vistedplaces: 
        vistedplaces.add(root)
        print(root)

        for i in graph[root]:
            newR=i
            preorder(newR,graph,vistedplaces)

def postorder(root,graph,vistedplaces):
    if root not in vistedplaces:
        vistedplaces.add(root)

        for i in graph[root]:
            newR = i
            postorder(newR,graph,vistedplaces)
        print(root)


graph = {
    "A":["H","B","F","C"],
    "B":["A","D","S"],
    "C":["A","Q","E"],
    "D":["B"],
    "E":["C"],
    "F":["A","T"],
    "H":["A","I"],
    "I":["H"],
    "Q":["C"],
    "S":["B"],
    "T":["F"]    
}

root = "A"
vistedplaces = set()
# preorder(root, graph,visitedPlaces)
postorder(root, graph,vistedplaces)