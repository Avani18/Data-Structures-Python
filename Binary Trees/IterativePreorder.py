#Iterative version of Preorder Traversal

#Class for creating nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key
		
#Function to print Preorder Traversal
def preorder(root):
	
	#Initialise empty stack
	stack = []
	#Append root node to stack
	stack.append(root)
	
	#While length of stack is not zero
	while (stack):
		#Pop the element
		temp = stack.pop()
		#Print its value
		print (temp.data, end = ' ')
		
		#If right child exists
		if (temp.right):
			#Push it to stack
			stack.append(temp.right)
			
		#If left child exists
		if (temp.left):
			#Push it to stack
			stack.append(temp.left)
			
	print ()
						
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print ("Preorder traversal of the tree is: ")
preorder(root)
