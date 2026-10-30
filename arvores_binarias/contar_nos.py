from node import Node

def contar_nos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nos(raiz.left) + contar_nos(raiz.right)

