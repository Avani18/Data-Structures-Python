#Appending a node at the end of the Linked List

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
	
	llist.head= Node(2)
	second= Node(4)
	third= Node(6)
	
	llist.head.next= second
	second.next= third
	
	print ("Original list")
	llist.printList()
	print ("Adding a new node at the end")
	llist.append(8)
	print ("New node added")
	llist.printList()
