#Level Order Traversal of a tree using Recursion

#Class to create Nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
		
#Function to print Level Order Traversal  
def printLevelOrder(root):
	#Get height of tree
	h = height(root)
	print ("Height of tree = ",h)
	#Iterate whole tree level wise 
	for i in range(1, h+1):
		#Print nodes of particular level
		printGivenLevel(root, i)

#Function to print nodes of given level	
def printGivenLevel(root, level):
	#End of tree
	if root is None:
		return 
	#Level to be printed
	if level == 1:
		#Print value
		print (root.val)
	#Level greater
	elif (level>1):
		#Recursive call for left node
		printGivenLevel(root.left, level-1)
		#Recursive call for right node
		printGivenLevel(root.right, level-1)
	
#Function to get height of a tree	
def height(node):
	#End of tree
	if node is None:
		return 0
	#Continue iteration
	else:
		#Recursive call for left height
		lheight = height(node.left)
		#Recursive call for right height
		rheight = height(node.right)
		#Return the greater height as height of tree
		if (lheight>rheight):
			return lheight+1
		else:
			return rheight+1
			
#Create root node
root = Node(1) 

#Set left of root node
root.left = Node(2) 
#Set right of root node
root.right = Node(3) 

#Set left of left of root node
root.left.left = Node(4) 
#Set right of right of root node
root.left.right = Node(5) 
  
#Print the level order traversal
print ("Level order traversal of binary tree is:")
printLevelOrder(root) 				
