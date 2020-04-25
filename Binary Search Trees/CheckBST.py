#Convert a Binary Tree to a Binary Search Tree

#Class for creating nodes
class Node:
	
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	
#Function to store the Inorder traversal of a tree in an array
def storeInOrder(root, arr):
	if (root is None):
		return 
	
	#Recursive call to the left subtree	
	storeInOrder(root.left, arr)
	#Append the data to List
	arr.append(root.data)
	#Recursive call to the right subtree
	storeInOrder(root.right, arr)
	return arr
	
#Function to check if a tree is a BST or not
def checkBST(root):
	arr = []
	#Get the Inorder traversal
	new_arr = storeInOrder(root, arr)
	#If the array is in sorted order, it is a BST
	if (sorted(new_arr) == new_arr):
		print("It is a BST!")
	else: 
		print("It is not a BST!")
		
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
checkBST(root)
