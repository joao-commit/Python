from NodeLinkedList import Node

def inserir_meio(self, data, pos):
    newNode = Node(data)
    if pos < 0 or pos > self.length:
        return None
    
    if pos == 0:
        if self.legth == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return

    current = self . head
    for i in range ( pos ):
        current = current.next
    previous = current.prev
    newNode.next = current
    newNode.prev = previous
    previous.next = newNode
    current.prev = newNode
    self.length += 1