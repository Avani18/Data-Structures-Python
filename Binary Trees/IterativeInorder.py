#Iterative version of Inorder Traversal

#Class for creating nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key
		
#Function to print Inorder Traversal
def inorder(root):

	#Initialise stack
	stack = []
	#Set the current pointer to be root
	current = root
	
	while True:
		#Reach the left end of depth
		if (current is not None):
			#Append node to stack
			stack.append(current)
			#Move current pointer towards left
			current = current.left
		
		#For visiting the right side
		elif (stack):
			#Pop leftside element
			current = stack.pop()
			#Print its data
			print (current.data, end = ' ')
			#Move current to the right child
			current = current.right
			
		#Tree completed
		else:
			break
			
	print()
	
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print ("Inorder traversal of the tree is: ")
inorder(root)
