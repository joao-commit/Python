from NodeLinkedList import Node

def inserir_inicio(self, data):
    newNode = Node(data, None, None)
    if self.length == 0:
        self.head = newNode
    else:
        newNode.prev = None
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
    self.length += 1
