#Print Postorder traversal from Inorder and Preorder traversal

#Class for creating nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

#Function to print the postorder
def printPostorder(inorder, preorder, n):
	
	#First value of preorder is the root 
	#If root exists in inorder
	if (preorder[0] in inorder):
		#Assign value of index of root in inorder
		root = inorder.index(preorder[0])
	
	#Print left subtree
	if (root!=0):
		printPostorder(inorder[:root], preorder[1:root+1], len(inorder[:root]))
		
	#Print right subtree
	if (root != (n-1)):
		printPostorder(inorder[root + 1:], preorder[root + 1:], len(inorder[root + 1:]))
		
	#Print the root element at the end
	print (preorder[0], end = ' ')
	

inorder = [4,2,5,1,3,6]
preorder = [1,2,4,5,3,6]
n = len(inorder)
print ("Postorder traversal: ")
printPostorder(inorder, preorder, n)
print ('')
