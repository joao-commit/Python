class Dado:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Dado(data, self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("Stack underflow")
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def peek(self):
        if self.head is None:
            raise IndexError("Stack underflow")
        return self.head.data
        
    def isEmpty(self):
        return self.head is None