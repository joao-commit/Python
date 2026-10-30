def remover_inicio(self):
    if self.length == 0:
        return None
    if self.head == 1:
        self.head = None
    else:
        self.head = self.head.next
        self.head.prev = None
    self.length -= 1