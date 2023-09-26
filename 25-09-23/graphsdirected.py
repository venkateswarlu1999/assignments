class graph:
    def __init__(self,numofNodes):
        self.numofNodes = numofNodes
        self.adjMatrix = []
        for i in range(numofNodes):
            row = [0]*numofNodes
            self.adjMatrix.append(row)
            
    def addEdge(self,vol1,vol2):
        self.adjMatrix[vol1][vol2] = 1
        # self.adjMatrix[vol2][vol1] = 1
    
    def display(self):
        for i in self.adjMatrix:
            print(i)
            
g=graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,3)
g.addEdge(1,3)
g.addEdge(1,2)
g.display()