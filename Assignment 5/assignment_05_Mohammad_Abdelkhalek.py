class Node:
    
    def __init__(self, value, parent=None, right=None, left=None):
        self.parent = parent
        self.right = right
        self.left = left
        self.value = value
        
class BST:
    
    def __init__(self):
        self.root = None