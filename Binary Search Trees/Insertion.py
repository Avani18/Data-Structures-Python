#Inserting a node in a Binary Search Tree

#Class for creating nodes
class Node:
	
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

#Function to insert a new node		
def insertNode(root, data):
	
	#If tree is empty
	if (root == None):
		#Initialise the root 
		root = Node(data)
	else: 
		#If new data is greater than root 
		if (root.data < data):
			#Check right child
			#If it does not exist
			if (root.right is None):
				#Set the new node to be right child
				root.right = Node(data)
			#If it exists
			else:
				#Recursively call function till node is inserted
				insertNode(root.right, data)
		
		#If new data is less than root		
		else:
			#Check left child
			#If it does not exist
			if (root.left is None):
				#Set the new node to be left child
				root.left = Node(data)
			#If it exists
			else:
				#Recursively call function till node is inserted
				insertNode(root.left, data)
				
#Function to print the Inorder traversal of a given tree		
def printInOrder(root):

	if (root is None):
		return
		
	printInOrder(root.left)
	print (root.data, end = ' ')
	printInOrder(root.right)
	
r = Node(50) 
insertNode(r,30) 
insertNode(r,20) 
insertNode(r,40) 
insertNode(r,70) 
insertNode(r,60) 
insertNode(r,80) 
  
# Print inoder traversal of the BST 
print ("The Inorder traversal of the generated BST is: ")
printInOrder(r)
print ()
