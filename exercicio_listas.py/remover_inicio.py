def remover_inicio(self):
    if self.length == 0:
        return None
    if self.length != 0:
        self.head = self.head.next
        self.length -= 1