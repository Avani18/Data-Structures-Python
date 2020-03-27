#Adding a node after a given node

#Class for making nodes
class Node:
	
	def __init__(self, data):
		self.data= data
		self.next= None
	
#Class for making a Linked List		
class LinkedList:

	def __init__(self):
		self.head= None
		
#Function to print the Linked List starting with the give node	
	def printList(self):
		temp= self.head
		while (temp):
			print (temp.data)
			temp= temp.next
			
#Function to add a node after a given node
#This function takes 2 parameters- The node after which the new node has to be inserted and the data of the new node
	def addNodeAfter(self, prev_node, new_data):
		#Check if prev_node is NULL
		if prev_node is None:
			print ("Previous node cannot be NULL")
			return 
		#Initialise the new node
		new_node= Node(new_data)
		#Link the new node to the next node using the next pointer of previous node
		new_node.next= prev_node.next
		#Link the new node to the previous node by making the previous node point to the new node
		prev_node.next= new_node
		
if __name__=='__main__':

	llist= LinkedList()
	
	llist.head= Node(2)
	second= Node(4)
	third= Node(8)
	
	llist.head.next= second
	second.next= third
	
	print ("Original list")
	llist.printList()
	print ("Adding new node in between")
	llist.addNodeAfter(second, 6)
	print ("New node added")
	llist.printList()
