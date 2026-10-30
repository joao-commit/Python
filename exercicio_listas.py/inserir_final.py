from NodeLinkedList import Node

def inserir_final(self, data):
    newNode = Node(data)

    if self.length == 0:
        self.head = newNode
        self.length += 1
        return
    
    current = self.head
    while current.next is not None:
        current = current.next
    current.next = newNode
    self.length += 1