#####################################
# Mohammad Abdelkhalek Assignment 4 #
#####################################

# Stacks and Queues

# Using Stack
def isPalindrome(string):
    
    string = ''.join(string.split()).lower()
    
    stack = []
    
    for i in string:
        stack.append(i)
        
    reversed = ''
    
    for i in range(len(stack)):
        reversed += stack.pop()
        
    if string == reversed:
        return True
    else:
        return False
    
# print(isPalindrome("Never odd or even"))

def isBalanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    
    for i in expression:
        if i in matching.values():
            stack.append(i)
        
        elif i in matching:
            if stack and stack[-1] == matching[i]:
                stack.pop()
                
            else:
                return False
    
    return not stack
    
# print(isBalanced("(1+2)-3*[41+6]"))


def decodeMIB(message):
    stack = []
    
    for i in message:
        if i == '*':
            if stack:
                stack.pop()
        else:
            stack.append(i)
            
    return ''.join(stack)

# print(decodeMIB("SIVLE****** DAED TNSI ***"))






        

        
    