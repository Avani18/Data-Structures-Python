#Ading a node to the front of the Linked List

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
			
if __name__=='__main__':
	
	llist= LinkedList()
	
	llist.head= Node(4)
	second= Node(6)
	third= Node(8)
	
	llist.head.next= second
	second.next= third
	
	print ("Original List")
	llist.printList()
	print ("Adding a new node at the front")
	llist.push(2)
	print ("Added new node as head")
	llist.printList()
