class Node:
    val : int
    def __init__(self, val):
        self.val = val




class Graph:
    nums = [Node]
    matrix = [int][int]

    def addNode(self, node:Node):
        self.nums.append(node)

    def addEdge(self, src, dest):
        self.matrix.append(src, dest)

