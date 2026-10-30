class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def setData( self , data ):
        self.data = data
    def getData( self ):
        return self.data
    def setNext( self , next ):
        self.next = next
    def getNext( self ):
        return self.next
    def hasNext( self ):
        return self.next is not None
    def setPrev( self , prev ):
        self.prev = prev
    def getPrev( self ):
        return self.prev
    def hasPrev( self ):
        return self.prev is not None
    
class LinkedList:
    def __init__( self ):
        self.length = 0
        self.head = None
    def setHead( self , node ):
        self.head = node
    def getHead( self ):
        return self.head