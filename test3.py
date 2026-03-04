# middle of linked list

class LinkedNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def getLength(headNode:LinkedNode) -> int:

    node = headNode.next
    count  = 0
    while node != None:
        count +=1
        node = node.next

    return count

def getMidNode(headNode:LinkedNode, count:int) -> LinkedNode:

    midcount = count//2
    print(midcount)
    tempCount  = 0
    node = headNode
    while tempCount  != midcount:
        tempCount +=1
        node = node.next

    print(node.val)
    return node

def reverseNode(headNode: LinkedNode):
    preNode = LinkedNode(0)
    preNode.next = headNode

    preNode.next = headNode
    




if __name__ == "__main__":
    head = LinkedNode(10)
    second = LinkedNode(20)
    third = LinkedNode(30)

    head.next  = second
    second.next = third

    print(getMidNode(head, getLength(head)).val)

