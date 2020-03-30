#Performing all the insertions in a single program

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
			
#Function to add a node to the front of the Linked List
#Thiis takes a parameter of the new data only as it can access the Linked List as a member of its class		
	def push(self, new_data):
		#Create new node
		new_node= Node(new_data)
		#Set pointer of new head to existing head
		new_node.next= self.head
		#Set new node as head
		self.head= new_node
		
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
		
#Function to append a node at the end of the Linked List
#This function takes the data of the new node as the parameter
	def append(self, new_data):
		#Initialise a new node
		new_node= Node(new_data)
		
		#Check if the Linked List is empty 
		if (self.head is None):
			#If yes, set the new node as the head node
			self.head= new_node
			return
			
		#Iterate to the last node of the Linked List 
		last= self.head
		while (last.next):
			last= last.next
			
		#Link the new node to the last node
		last.next= new_node
		
if __name__=='__main__':
	
	llist= LinkedList()
	
	# 6
	llist.append(6)
	# 7->6
	llist.push(7)
	# 1->7->6
	llist.push(1)
	# 1->7->6->4
	llist.append(4)
	# 1->7->8->6->4
	llist.addNodeAfter(llist.head.next, 8)
	
	print ("Created list is: ")
	llist.printList()
