#Construct a tree from given Inorder and Preorder traversals

#Class to create nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

#Function to build a tree from Inorder and Preorder traversals
#It takes 4 parameters- inorder traversal, preorder traversal, start index (0), end index (length of tree - 1)		
def buildTree(inorder, preorder, instart, inend):
	
	#If start index is greater than end index (Tree completed)
	if (instart > inend):
		return None
		
	#Create a node using preIndex (used to iterate the preorder traversal)
	temp = Node(preorder[buildTree.preIndex])
	#Increment the preIndex
	buildTree.preIndex += 1
	
	#If start index = end index (this node has no children)
	if (instart == inend):
		return temp 
		
	#Else, find the index of this node in Inorder traversal
	inIndex = search(inorder, instart, inend, temp.data)
	
	#Construct left subtree recursively 
	temp.left = buildTree(inorder, preorder, instart, inIndex - 1)
	#Construct right subtree recursively
	temp.right = buildTree(inorder, preorder, inIndex + 1, inend)
	
	return temp
	
#Function to find the index of a certain value 
#It takes 4 parameters- list of the order, start index of list, end index of list, value whose index is to be found
def search(arr, start, end, value):
	#Iterate the whole list
	for i in range(start, end + 1):
		#If match is found
		if (arr[i] == value):
			#Return index
			return i
	
#Function to print the Inorder traversal of a given tree		
def printInOrder(root):

	if (root is None):
		return
		
	printInOrder(root.left)
	print (root.data, end = ' ')
	printInOrder(root.right)
	
inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 

#Initialise the preIndex variable
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1) 
  
print ("Inorder traversal of the constructed tree is: ")
printInOrder(root) 
print()
