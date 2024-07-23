class Node:
    
    def __init__(self, value, parent=None, right=None, left=None):
        self.parent = parent
        self.right = right
        self.left = left
        self.value = value
        
class BST:
    
    def __init__(self):
        self.root = None
        
    def addHelper(self, n, current):
        if current.value > n.value:  # go to left
            if current.left is None:  # current does not have a left child
                current.left = n
                n.parent = current
            else:
                self.addHelper(n, current.left)
        else:  # go to right
            if current.right is None:
                current.right = n
                n.parent = current
            else:
                self.addHelper(n, current.right)
                
    def add(self, value):
        n = Node(value)
        if self.root is None:  # tree is empty
            self.root = n
        else:
            self.addHelper(n, self.root)
            
    def inOrder(self, current):
        if current is None:
            return
        self.inOrder(current.left)
        print(current.value)
        self.inOrder(current.right)