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


# Linked Lists - removing a node at a given location

class Node:

  def __init__(self, info, next):
    self.info = info
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0  # how many nodes are in my LL

  def addToHead(self, info):  # O(1)
    n = Node(info, None)
    if self.size == 0:  # LL is empty, I have no nodes inside
      self.head = n
      self.tail = n
      self.size = 1
    else:
      n.next = self.head
      self.head = n
      self.size += 1

  def addToTail(self, info):  # O(1)
    if self.size == 0:
      self.addToHead(info)
    else:
      n = Node(info, None)
      self.tail.next = n
      self.tail = n
      self.size += 1

  def deleteHead(self):  # O(1)
    if self.size == 0:  # empty
      return None
    elif self.size == 1:
      val = self.head.info
      self.head = None
      self.tail = None
      self.size = 0
      return val
    else:
      val = self.head.info
      self.head = self.head.next
      self.size -= 1
      return val

  def deleteAtLocation(self, pos):  # O(n)
    if pos < 0 or pos >= self.size:
      return None  # Invalid position

    if pos == 0:
      return self.deleteHead()
    elif pos == self.size - 1:
      return self.deleteTail()
    else:
      prev = None
      current = self.head
      count = 0
      while count < pos:
        prev = current
        current = current.next
        count += 1

      # Now current is the node to be deleted
      val = current.info
      prev.next = current.next
      self.size -= 1
      return val

  def printLL(self):  # O(n)
    i = self.head
    while i != None:
      print(i.info, "->", end="")
      i = i.next
    print()

  def deleteTail(self):  # O(n)
    if self.size <= 1:
      return self.deleteHead()
    else:
      val = self.tail.info
      # loop to find the element before the last
      i = self.head
      while i.next.next != None:  # I did not reach the node before the last
        i = i.next
      # update the tail and its next
      self.tail = i
      self.tail.next = None
      self.size -= 1
      return val




        

        
    