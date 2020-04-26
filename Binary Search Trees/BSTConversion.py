#Convert a Binary Tree to a Binary Search Tree

#Class for creating nodes
class Node:
	
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		
#Function to print the Inorder traversal of a given tree		
def printInOrder(root):

	if (root is None):
		return
		
	printInOrder(root.left)
	print (root.data, end = ' ')
	printInOrder(root.right)
	
#Function to store the inorder traversal in an array
#inorder is the array of inorder traversal
def storeInOrder(root, inorder):
	
	if (root is None):
		return
		
	#Recursive call to the left subtree
	storeInOrder(root.left, inorder)
	#Append the value to array 
	inorder.append(root.data)
	#Recursive call to the right subtree
	storeInOrder(root.right, inorder)

#Function to convert a sorted array to a Binary Search Tree
def arrayToBST(arr, root):
	
	if (root is None):
		return 
		
	#Recursive call to make the left subtree
	arrayToBST(arr, root.left)
	#Update the data of the root
	root.data = arr[0]
	#Delete its value from the array
	arr.pop(0)
	#Recursive call to make the right subtree
	arrayToBST(arr, root.right)
	
#Function to convert the Binary Tree to a Binary Search Tree	
def binaryTreeToBST(root):
	
	if (root is None):
		return 
		
	#Initialise an empty list for inorder traversal
	arr = []
	#Store it in array
	storeInOrder(root, arr)
	#Sort the array in ascending order
	arr.sort()
	#Convert the sorted array to BST
	arrayToBST(arr, root)
	
	
root = Node(10)

root.left = Node(30)
root.right = Node(15)

root.left.left = Node(20)
root.right.right = Node(5)

print("Inorder traversal of the Binary Tree is:")
printInOrder(root)
print()

print("Converting it to a Binary Search Tree")
binaryTreeToBST(root)

print("Inorder traversal of the Binary Search Tree is: ")
printInOrder(root)
print()
