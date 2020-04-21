#Iterative version of Postorder Traversal

#Class for creating nodes
class Node:
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key
		
#Function to print Postorder Traversal
def postorder(root):

	stack1 = []
	stack2 = []
	stack1.append(root)
	
	while (stack1):
		
		temp = stack1.pop()
		stack2.append(temp)
		
		if (temp.left):
			stack1.append(temp.left)
		if (temp.right):
			stack1.append(temp.right)
			
	while (stack2):
		
		print (stack2.pop().data, end = ' ')
		
	print ()
		
root = Node(1) 

root.left = Node(2) 
root.right = Node(3) 

root.left.left = Node(4) 
root.left.right = Node(5) 

root.right.left = Node(6) 
root.right.right = Node(7)
			
print ("Postorder traversal of binary tree is:")
postorder(root)
