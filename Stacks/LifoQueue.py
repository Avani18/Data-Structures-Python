#Implementing stacks using LifoQueue class from queue module

from queue import LifoQueue

stack= LifoQueue(maxsize=4)

print ("Number of elements in stack: ",stack.qsize())

print('Pushing elements to the stack') 
stack.put(2) 
stack.put(4) 
stack.put(6)
stack.put(8)

print ("Full: ", stack.full())
print ("Size: ", stack.qsize())

print('Elements popped from the stack') 
print(stack.get()) 
print(stack.get()) 
print(stack.get()) 
print(stack.get()) 
  
print("Empty: ", stack.empty())
