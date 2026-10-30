from node import Node

raiz = Node(10)
raiz.set_left(5)
raiz.set_right(15)

print(f"A raiz é: {raiz.data}")
print(f"O filho esquerdo é: {raiz.left.data}")
print(f"O filho direito é: {raiz.right.data}")