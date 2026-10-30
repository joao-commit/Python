def encontre_maior(raiz, max):
    if raiz is None:
        return max
    
    if max < raiz.data:
        max = raiz.data

    if raiz.left is not None:
        temp = encontre_maior(raiz.left, max)
        if max < temp:
            max = temp

    if raiz.right is not None:
        temp = encontre_maior(raiz.right, max)
        if max < temp:
            max = temp
            
    return max