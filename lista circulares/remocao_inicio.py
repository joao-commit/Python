def remover_inicio(self):
    if self.head is None:
        return
    if self.head == self.head:
        self.head = None
    else:
        current = self.head
        while current.next is not self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next