from NodeLinkedList import Node

def inserir_final(self, data):
    newNode = Node(data)
    if self.length == 0:
        self.head = newNode
    else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode
        newNode.prev = current.next
        newNode.next = None
    self.length += 1