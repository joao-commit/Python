from NodeLinkedList import Node

def posicao_especifica(self, data, posicao):
    if posicao > self.length or posicao < 0:
        return None
    
    newNode = Node(data)
    
    if posicao == 0:
        newNode.next = self.head
        self.head = newNode
    else:
        current = self.head
        for i in range(posicao - 1):
            current = current.next
        newNode.next = current.next
        current = newNode
    self.length += 1
