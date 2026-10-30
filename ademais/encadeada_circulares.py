def tranformacao_circular(self):
    tamanho = 0
    atual = self.head

    while atual is not None:
        atual = atual.next
        tamanho += 1
        
    if tamanho == 0:
        return None, None
    
    meio = tamanho // 2

    atual = self.head
    count = 0

    head1 = atual
    prev = None

    while count < meio:
        prev = atual
        atual = atual.next
        count += 1

    if prev:
        prev.next = head1

    head2 = atual
    prev2 = None

    while atual is not None:
        prev2 = atual
        atual = atual.next

    if prev2:
        prev2.next = head2

    return head1, head2