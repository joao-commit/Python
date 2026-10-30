def remover_final(self):
    if self.length == 0:
        return None
    if self.length == 1:
        self.head = None
    else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None
    self.length -= 1