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
    