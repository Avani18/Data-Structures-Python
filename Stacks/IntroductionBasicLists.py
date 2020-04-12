#Implementing the basic functions of a stack using Lists

#To return infinte in case of empty stack
from sys import maxsize

#Function to create a stack using lists
def createStack():
	stack= []
	return stack

#Function to check if stack is empty	
def isEmpty(stack):
	#If length of stack is 0, it is empty
	return len(stack)==0

#Function to push an element to the stack	
def push(stack,item):
	#Append item at the end of the list 
	stack.append(item)
	print (item+ " pushed to the stack")
	
#Function to pop an element from the stack	
def pop(stack):
	#Check if the stack is already empty
	if (isEmpty(stack)):
		print ("Cannot pop because stack is empty!")
		#Return negative infinite value
		return str(-maxsize -1)	
	#If stack is not empty, pop the last element and return it 
	return stack.pop()
	
#Function to peek the stack
def peek(stack):
	#Check if the stack is already empty
	if (isEmpty(stack)):
		print ("Cannot peek because stack is empty!")
		#Return negative infinite value
		return str(-maxsize -1)
	#Return the last value of the list 
	return stack[-1]
	
#Main code
#Create a stack
stack= createStack()
#Push an element to the stack
push(stack, str(10))
#Push an element to the stack
push(stack, str(20))
#Push an element to the stack
push(stack, str(30))
#Pop an element from the stack
print (pop(stack)+" popped from stack")
#Peek an element from the stack
print (peek(stack)+ " peeked from stack")
