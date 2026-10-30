class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, data):
        self.left = Node(data)
        self.left.parent = self
        return self.left
    
    def set_right(self, data):
        self.right = Node(data)
        self.right.parent = self
        return self.right
