#Introduction to Binary Trees

#Class to create Nodes of the tree
class Node:

#Constructor
	def __init__(self,key):
		#Set the left pointer 
		self.left = None
		#Set the right pointer
		self.right = None
		#Set the value of the node
		self.val = key
		
#Create root node
root = Node(2)

#Set the left of root
root.left = Node(4)
#Set the right of root
root.right = Node(6)

#Set the left of left of root
root.left.left = Node(8)

'''Final tree 
           2 
       /       \ 
      4          6 
    /   \       /  \ 
   8    None  None  None 
  /  \ 
None None'''
