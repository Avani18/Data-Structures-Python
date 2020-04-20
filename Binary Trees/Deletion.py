#Deletion of a node and replace it with deepest rightmost node of the tree

#Class to create nodes 
class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

#Inorder traversal of a binary tree 
def inorder(temp): 
	if (not temp): 
		return
	inorder(temp.left) 
	print (temp.data, end = " ") 
	inorder(temp.right) 

#Function to delete the deepest node in binary tree 
def deleteDeepest(root, d_node): 
	#Queue to iterate the tree
	q = []
	#Append the root node to queue 
	q.append(root) 
	#Iterate the tree till deepest node is found
	while(len(q)): 
		#Remove the first node from the queue
		temp = q.pop(0)
		#Check if deepest node is found
		if (temp is d_node): 
			#Remove the node
			temp = None
			return
		#If right child exists
		if (temp.right): 
			#If the child is the deepest node
			if (temp.right is d_node):
				#Remove the node 
				temp.right = None
				return
			#If it is not the deepest node, add to the queue 
			else: 
				q.append(temp.right) 
		#If left child exists
		if (temp.left): 
			#If the child is the deepest node
			if (temp.left is d_node):
				#Remove the node 
				temp.left = None
				return
			#If it is not the deepest node, add to the queue 
			else: 
				q.append(temp.left) 

#Function to delete an element from the binary tree 
def deletion(root, key): 
	#If tree is empty
	if (root == None): 
		return None
	#If root node is the only node
	if (root.left == None and root.right == None): 
		#Required node found
		if (root.data == key): 
			#Empty tree after deletion
			return None
		#Required node not found
		else : 
			#Return tree as it is
			return root 
			
	#Node to be deleted
	key_node = None
	#Queue to iterate the list
	q = [] 
	#Add the root node to queue
	q.append(root) 
	
	#Iterate the whole tree
	while(len(q)): 
		#Remove the first element of queue
		temp = q.pop(0)
		#If node is found 
		if (temp.data == key): 
			key_node = temp 
		#If left child exists
		if (temp.left): 
			#Add to queue
			q.append(temp.left) 
		#If right child exists
		if (temp.right): 
			#Add to queue
			q.append(temp.right) 
	
	#Now temp node is the deepest rightmost node
	#If node to be deleted is found
	if (key_node): 
		#Data of deepest node
		x = temp.data
		#Delete the deepest node
		deleteDeepest(root,temp) 
		#Change data of node that had to be deleted
		key_node.data = x 
	#Return root node
	return root 
 
if __name__=='__main__': 

	root = Node(10) 
	
	root.left = Node(11) 
	root.right = Node(9)
	
	root.left.left = Node(7) 
	root.left.right = Node(12)  
	
	root.right.left = Node(15) 
	root.right.right = Node(8) 
	
	print("The tree before the deletion: ") 
	inorder(root)
	 
	root = deletion(root, 11) 
	print()
	 
	print("The tree after the deletion;") 
	inorder(root) 
