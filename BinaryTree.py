class Node :
    val : int
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if __name__ == "__main__":

    root = Node(10)
    node_5 = Node(5)
    node_15 = Node(15)
    node_2 = Node(2)
    node_7 = Node(7)

    root.left =  node_5
    root.right = node_15

    






