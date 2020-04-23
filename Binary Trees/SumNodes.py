#Calculate the sum of all nodes in a binary tree

#Class to create nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

#Function to calculate the sum of nodes		
def sumNodes(root):
	#If tree is empty
	if (root == None):
		#Return 0
		return 0
	#Add value of root and recursively calculate sum of left subtree and right subtree 
	return (root.data + sumNodes(root.left) + sumNodes(root.right))
	
root = Node(1)  

root.left = Node(2)  
root.right = Node(3)  

root.left.left = Node(4)  
root.left.right = Node(5)  

root.right.left = Node(6)  
root.right.right = Node(7)  

root.right.left.right = Node(8)   
  
print("Sum of all the nodes of the binary tree is: ", sumNodes(root))	
	
