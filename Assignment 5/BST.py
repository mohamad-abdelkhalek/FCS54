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
        
    def preOrder(self, current):
        if current is None:
            return
        print(current.value)
        self.preOrder(current.left)
        self.preOrder(current.right)
    
    def postOrder(self, current):
        if current is None:
            return
        self.postOrder(current.left)
        self.postOrder(current.right)
        print(current.value)
        
    def findMin(self, current):
        while current.left is not None:
            current = current.left
        return current
    
    def deleteNode(self, current, value):
        if current is None:
            return current
        
        if value < current.value:
            current.left = self.deleteNode(current.left, value)
        elif value > current.value:
            current.right = self.deleteNode(current.right, value)
        else:
            # Node with only one child or no child
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.findMin(current.right)
            
            # Copy the inorder successor's content to this node
            current.value = temp.value
            
            # Delete the inorder successor
            current.right = self.deleteNode(current.right, temp.value)
        
        return current