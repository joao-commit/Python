def remover_meio(self, pos):
    if pos < 0 or pos >= self.length:
        return None
    if pos == 0:
        if self.length == 0:
            return None
        else:
            self.head = self.head.next
            self.head.prev = None
    else:
        current = self.head
        for i in range(pos - 1):
            current = current.next
        pulo = current.next
        current.next = pulo.next
        if pulo.next is not None:
            pulo.next.prev = current
    self.length -= 1
    