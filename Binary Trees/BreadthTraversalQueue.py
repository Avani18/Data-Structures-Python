#Level Order Traversal of a tree using Queues

#Class to create nodes
class Node:
		
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
		
#Function to print the Level Order Traversal 
def printLevelOrder(root):

	#If tree is empty
	if (root is None):
		return
	
	#Initialise the queue	
	queue = []
	#Add the root node to queue
	queue.append(root)
	
	#Iterate the whole tree till all nodes are covered
	while (len(queue) > 0):
		#Print the node value
		print (queue[0].val)
		#Remove the printed node
		node = queue.pop(0)
		#If there is a left child
		if (node.left is not None):
			#Append it to the queue
			queue.append(node.left)
		#If there is a right child	
		if (node.right is not None):
			#Append it to the queue
			queue.append(node.right)
			
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.right.left = Node(5)

#Print the level order traversal
print ("Level order traversal of binary tree is: ")
printLevelOrder(root)
