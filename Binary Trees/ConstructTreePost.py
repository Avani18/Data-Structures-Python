#Construct a tree from given Inorder and Preorder traversals

#Class to create nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

#Function to construct the tree
#It takes 4 parameters- inorder traversal, postorder traversal, start index (0), end index (length - 1), index array of postorder		
def build(inorder, postorder, instart, inend, pIndex):
	
	#If start index is greater than end index (Tree completed)
	if (instart > inend):
		return None
		
	#Create a node using pIndex (used to iterate the preorder traversal)
	temp = Node(postorder[pIndex[0]])
	#Decrement
	pIndex[0] -= 1
	
	#If start index = end index (this node has no children)
	if (instart == inend):
		return temp 
		
	#Else, find the index of this node in Inorder traversal	
	iIndex = search(inorder, instart, inend, temp.data)
	
	#Construct left subtree recursively
	temp.right = build(inorder, postorder, iIndex + 1, inend, pIndex)
	#Construct right subtree recursively
	temp.left = build(inorder, postorder, instart, iIndex - 1, pIndex)
	
	return temp

#Funtion to initialise the index of root and build the tree
#It takes 3 parameters- inorder traversal, postorder traversal, lenght of tree	
def buildTree(inorder, postorder, n):
	#Initialise pIndex
	pIndex = [n-1]
	#Call build function
	return build(inorder, postorder, 0, n - 1, pIndex)
	
#Function to find the index of a certain value 
#It takes 4 parameters- list of the order, start index of list, end index of list, value whose index is to be found
def search(arr, start, end, value):
	#Iterate the whole list
	for i in range(start, end + 1):
		#If match is found
		if (arr[i] == value):
			#Return index
			return i
			
#Function to print the Preorder traversal of a given tree		
def printPreOrder(root):

	if (root is None):
		return
		
	print (root.data, end = ' ')
	printPreOrder(root.left)
	printPreOrder(root.right)
	
	
inorder = [4, 8, 2, 5, 1, 6, 3, 7] 
postorder = [8, 4, 5, 2, 6, 7, 3, 1]  

n = len(inorder) 

root = buildTree(inorder, postorder, n)  
  
print("Preorder of the constructed tree: ")  
printPreOrder(root) 
print ()
