#Declaring nodes and assigning them values

#Class for making nodes
class Node:
	
	#Initialize the object of the Node
	def __init__(self, data):
		self.data= data
		self.next= None

#Class for making a Linked List		
class LinkedList:

	#Initialize a Linked List with the head node
	def __init__(self):
		self.head= None
		
if __name__=='__main__':

	#Declare a LinkedList
	llist= LinkedList()
	
	#Set head for the Linked List
	llist.head= Node(1)
	
	#Declare other node
	second= Node(2)
	third= Node(3)
	
	#Link all the nodes
	llist.head.next= second
	second.next= third
