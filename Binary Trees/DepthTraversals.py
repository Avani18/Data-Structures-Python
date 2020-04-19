#Inorder, Postorder and Preorder traversals of Binary tree

#Class for creating nodes
class Node:
	
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
		
#Function to print the Inorder(left,root,right) traversal		
def printInorder(root):
	#Iterate the tree till end	
	if (root):
		#Recursive call to left child
		printInorder(root.left)
		#Print root value
		print (root.val)
		#Recursive call to right child
		printInorder(root.right)
			
#Function to print the Postorder(left,right,root) traversal
def printPostorder(root):
	#Iterate the tree till end
	if (root):
		#Recursive call to left child
		printPostorder(root.left)
		#Recursive call to right child
		printPostorder(root.right)
		#Print root value
		print (root.val)

#Function to print the Preorder(root,left,right) traversal			
def printPreorder(root):
	#Iterate the tree till end
	if (root):
		#Print root value
		print (root.val)
		#Recursive call to left child
		printPreorder(root.left)
		#Recursive call to right child
		printPreorder(root.right)
			
#Create root node
root = Node(2)

#Set left of root node
root.left = Node(4)
#Set right of root node
root.right = Node(6)

#Set left of left of root node
root.left.left = Node(8)
#Set right of right of root node
root.right.right = Node(10)

#Print the inorder traversal
print ("Inorder traversal of binary tree is: ")
printInorder(root)

#Print the postorder traversal
print ("Postorder traversal of binary tree is: ")
printPostorder(root)

#Print the preorder traversal
print ("Preorder traversal of binary tree is: ")
printPreorder(root)
