# Edge list
graph = [[0, 2], [2, 3], [2, 1], [1, 3]] # Descripes the edges between nodes

# Adjancent List
graph = [[2], [2, 3], [0, 1 , 3], [1, 2]] # The index is the value of a node

# Adjancent Matrix
graph = {
    0: [0,0,1,0],
    1: [0,0,1,1],
    2: [1,1,0,0],
    3: [0,1,1,0],
}
# # Edge list
# graph = [[0, 2, 'w'], [2, 3, 'w'], [2, 1, 'w'], [1, 3, 'w']] # Descripes the edges between nodes

# # Adjancent List
# graph = [[(2, 'w')], [(2, 'w'), (3, 'w')], [(0, 'w'),(1, 'w') , (3, 'w')], [(1, 'w'), (2 , 'w')]] # The index is the value of a node

# # Adjancent Matrix
# graph = {
#     0: [0,0,'w',0],
#     1: [0,0,'w','w'],
#     2: ['w','w',0,0],
#     3: [0,'w','w',0],
# }

class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes+=1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ''
            for vertex in nodeConnections:
                connections += vertex + " "
            print(node+" --> "+connections)

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()