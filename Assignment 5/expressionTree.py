class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printEquation(root):
    # Helper function for in-order traversal
    def inorder(node):
        if node is None:
            return ""
        
        if node.left is None and node.right is None:
            return str(node.value)
        
        left_expr = inorder(node.left)
        right_expr = inorder(node.right)
        
        return "(" + left_expr + str(node.value) + right_expr + ")"
    
    equation = inorder(root)
    
    # Removing the outermost parentheses
    if equation[0] == '(' and equation[-1] == ')':
        equation = equation[1:-1]
    
    return equation