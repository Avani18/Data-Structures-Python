#Searching a node in a Binary Search Tree

#Class for creating nodes
class Node:
	
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	
#Function to insert a new node		
def insertNode(root, data):
	
	if (root == None):
		root = Node(data)
	else: 
	
		if (root.data < data):
			if (root.right is None):
				root.right = Node(data)
			else:
				insertNode(root.right, data)
				
		else:
			if (root.left is None):
				root.left = Node(data)
			else:
				insertNode(root.left, data)	
	
#Function to search a node in the tree
def search(root, data):

	#If the root is None or the required match is found
	if (root is None or root.data == data):
		return root 
		
	#If data is less than root, move to left
	if (root.data > data):
		#Recursive call to function
		return search(root.left, data)
		
	#If data is greater than root, move to right and call function 
	return search(root.right, data)
		
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
print ("Searching for 40 in tree: ", search(r, 40))
print ("Searching for 10 in tree: ", search(r, 10))
