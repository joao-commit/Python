def inserir_final(self, data):
    newNode = Node(data)
    if self.length == 0:
        self.head = newNode
        newNode.next = self.head
    current = self.head
    while current.next is not self.head:
        currente = current.next
    currente.next = newNode
    newNode.next = self.head
    self.length += 1