from NodeLinkedList import Node

def inserir_inicio(self, data):
    newNode = Node(data)
    if self.length == 0:
        self.head = newNode  
    else:
        newNode.next = self.head
        self.head = newNode
    self.length += 1
