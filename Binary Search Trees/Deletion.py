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
	
#Get the minimum value node in a BST 
def minValue(root):

	current = root
	while (current.left is not None):
		current = current.left
		
	return current 
	
#Delete the node with given data
def deleteNode(root, data):

	#If root is none
	if (root is None):
		return root
		
	#If required data is less than root
	if (data < root.data):
		#Recursive call to left subtree
		root.left = deleteNode(root.left, data)
		
	#If required data is greater than root 
	elif (data > root.data):
		#Recursive call to right subtree
		root.right = deleteNode(root.right, data)
		
	#Required data is found
	else:
		#For nodes with 0 or 1 child
		#Check if node has left child
		if (root.left is None):
			temp = root.right
			root = None
			return temp
			
		#Check if node has right child
		elif (root.right is None):
			temp = root.right
			root = None
			return temp
			
		#For nodes with 2 children
		#Get the smallest value in right subtree (inorder successor)
		temp = minValue(root.right)
		#Copy its content to this node
		root.data = temp.data 
		#Delete the inorder successor node 
		root.right = deleteNode(root.right, temp.data)
		
	return root

#Function to print the Inorder traversal of a given tree		
def printInOrder(root):

	if (root is None):
		return
		
	printInOrder(root.left)
	print (root.data, end = ' ')
	printInOrder(root.right)

		
root = Node(50) 
insertNode(root, 30) 
insertNode(root, 20) 
insertNode(root, 40) 
insertNode(root, 70) 
insertNode(root, 60) 
insertNode(root, 80) 
  
print ("Inorder traversal of the given tree")
printInOrder(root) 
print()
  
print ("\nDelete 20")
root = deleteNode(root, 20) 
print ("Inorder traversal of the given tree after deletion of 20")
printInOrder(root) 
print()

print ("\nDelete 30")
root = deleteNode(root, 30) 
print ("Inorder traversal of the given tree after deletion of 30")
printInOrder(root) 
print()

print ("\nDelete 50")
root = deleteNode(root, 50) 
print ("Inorder traversal of the given tree after deletion of 50")
printInOrder(root) 
print()
