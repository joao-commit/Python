def remover_especifica(self, pos):
    if pos < 0 or pos >= self.length:
        return None
    if pos == 0:
        self.head = self.head.next
        self.length -= 1
        return
    
    current = self.head
    for i in range(pos - 1):
        current = current.next
    
    pulo = current.next
    current.next = pulo.next
    self.length -= 1