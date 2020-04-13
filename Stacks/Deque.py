#Implementing stacks using deque class from Collections module

#Import the required module
from collections import deque

#Create a stack
stack= deque()

#Push elements to the stack
stack.append(2)
stack.append(4)
stack.append(6)
stack.append(8)

print ("Initial stack:")
print (stack)

#Pop elements from the stack
print('\nElements popped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are popped:') 
print(stack)
