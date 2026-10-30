def remover(pilha):
    if pilha.isEmpaty():
        return
    pilha.pop()
    remover(pilha)
