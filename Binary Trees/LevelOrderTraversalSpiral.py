#Level order traversal in spiral order

#Class for creating nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key
		
#Function to print the spiral order of tree
def printSpiral(root):

	#If tree is empty
	if (root == None):
		print ("Tree is empty!")
		return 
	
	#Stack to print level from right to left	
	stack1 = []
	#Stack to print level from left to right
	stack2 = []
	
	#Append the root node (first level)
	stack1.append(root)
	
	#Iterate the whole tree
	while (not len(stack1) == 0 or not len(stack2) == 0):
		#Print nodes of current level from stack1 and append nodes of next level to stack2
		while (not len(stack1) == 0):
			#Last node of stack1
			temp = stack1[-1]
			#Pop the node 
			stack1.pop()
			#Print its data
			print (temp.data, end = ' ')
			
			#Append nodes of next level to stack2
			#Right is appended before left
			#If right child exists
			if (temp.right):
				#Append to stack2
				stack2.append(temp.right)
			#If left child exists
			if (temp.left):
				#Append to stack2
				stack2.append(temp.left)
		
		#Print nodes of current level from stack2 and append nodes of next level to stack1		
		while (not len(stack2) == 0):
			#Last node of stack2
			temp = stack2[-1]
			#Pop the node
			stack2.pop()
			#Print its data
			print (temp.data, end = ' ')
			
			#Append nodes of next level to stack1 from left to right
			#If left child exists
			if (temp.left):
				#Append to stack1
				stack1.append(temp.left)
			#If right child exists
			if (temp.right):
				#Append to stack1
				stack1.append(temp.right)
	print ('')
	
if __name__ == '__main__':

	root = Node(1)
	
	root.left = Node(2)
	root.right = Node(3)
	
	root.left.left = Node(4)
	root.left.right = Node(5)
	
	root.right.left = Node(6)
	root.right.right = Node(7)
	
	print ("Spiral Order Traversal of the binary tree is: ")
	printSpiral(root)
