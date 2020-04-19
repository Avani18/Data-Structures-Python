#Insertion at the first available position in the tree

#Class for creating nodes
class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

#Function to print the Level Order Traversal 
def printLevelOrder(root):

	if (root is None):
		return
	
	queue = []
	queue.append(root)
	
	while (len(queue) > 0):
		print (queue[0].val)
		node = queue.pop(0)
		if (node.left is not None):
			queue.append(node.left)
		if (node.right is not None):
			queue.append(node.right)
		
#Function to insert a node at the first available position in the tree
def insert(root, data):
	
	#If tree is empty
	if (root is None):
		#Set the root for tree
		root = Node(data)
		return
		
	#Initialise queue to iterate the tree
	queue = []
	#Append the root node
	queue.append(root)
	
	#Iterate the whole tree
	while (len(queue)):
		
		#Iterate tree through the temp node
		temp = queue[0]
		#Remove first node of the queue
		queue.pop(0)
		
		#If there is no left child
		if (not temp.left):
			#Insert new node
			temp.left = Node(data)
			break
		#Left child exists
		else:
			#Append to the queue
			queue.append(temp.left)
			
		#If there is no right child
		if (not temp.right):
			#Insert new node
			temp.right = Node(data)
			break 
		#Right child exists
		else:
			#Append to the queue
			queue.append(temp.right)
			
if __name__ == '__main__':
	
	root = Node(10)
	
	root.left = Node(20)
	root.right = Node(30)
	
	root.left.right = Node(50)
	root.right.left = Node(60)
	
	print ("Original Binary tree is: ")
	printLevelOrder(root)
	print ("Inserting node 40")
	insert(root, 40)
	printLevelOrder(root)
	print ("Inserting node 70")
	insert(root, 70)
	printLevelOrder(root)
