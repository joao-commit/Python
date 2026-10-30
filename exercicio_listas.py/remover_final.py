def remover_final(self):
    if self.length == 0:
        return None
    
    if self.length == 1:
        self.head = None
        self.length -= 1

    else:
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.length -= 1
