#Implementing the basic functions of a stack using Linked Lists

#Class to make a Stack node
class StackNode:
	
#Constructor to initialise the node
	def __init__(self, data):
		self.data= data
		self.next= None

#Class to create a stack		
class Stack:
	
#Constructor to initialise the stack with its top element
	def __init__(self):
		self.top= None
	
#Function to check if stack is empty	
	def isEmpty(self):
		#If there is no top element means that the stack is empty
		if (self.top is None):
			return True
		else: 
			return False
	
#Function to push an element to the stack		
	def push(self,data):
		#Create a new node
		new_node= StackNode(data)
		#Set the next of the new to the original top node
		new_node.next= self.top
		#Make the new node as the top node
		self.top= new_node
		print (data+" pushed to the stack")

#Function to pop an element from the stack			
	def pop(self):
	#Check if the stack is already empty
		if (self.isEmpty()):
			print ("Cannot pop because stack is already empty")
			#Return negative infinite value
			return str(float("-inf"))
		#Element to be removed
		temp= self.top
		#Set the new top of stack 
		self.top= temp.next
		#Return the data of popped node
		return temp.data

#Function to peek the stack		
	def peek(self):
	#Check if the stack is already empty
		if (self.isEmpty()):
			print ("Cannot peek because stack is already empty")
			#Return negative infinite value
			return str(float("-inf"))
		#Return the data of the top node
		return self.top.data
		
#Main code
#Create a stack
stack= Stack()
#Push an element to the stack
stack.push(str(10))
#Push an element to the stack
stack.push(str(20))
#Push an element to the stack
stack.push(str(30))
#Pop an element from the stack
print (stack.pop()+" popped from stack")
#Peek an element from the stack
print (stack.peek()+ " peeked from stack")
