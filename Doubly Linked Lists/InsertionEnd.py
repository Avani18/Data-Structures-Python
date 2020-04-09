#Insert a node at the end of the List

#Class for making nodes
class Node:

	def __init__(self, data= None, next= None, prev= None):
		self.next= next
		self.prev= prev
		self.data= data

#Class for making a Doubly Linked List	
class DoublyLinkedList:

	def __init__(self, head= None):
		self.head= head
	
#Function to print the List in forward direction	
	def printForward(self):
		
		if (self.head==None):
			print ("The List is empty!")
			return
	
		temp= self.head	
		while(temp):
			print (temp.data, end='\t')
			temp= temp.next
		print ('')	
	
#Function to print the List in backward direction
	def printBackward(self):
	
		if (self.head==None):
			print ("The List is empty!")
			return
			
		temp= self.head
		while(temp.next!=None):
			temp= temp.next
			
		while(temp):
			print (temp.data, end='\t')
			temp= temp.prev
		print ('')

#Function to insert a node at the end of the List
#This function takes 1 parameter- data of the new node to be added	
	def insertEnd(self, data):
	
		#Check if List is empty	
		if (self.head== None):
			print ("The List is empty!")
			return 
		
		#Node to iterate the List	
		temp= self.head
		#Create the new node
		new_node= Node(data)
		
		#Iterating the List to reach the last node
		while (temp.next):
			#Move the temp node
			temp= temp.next	
		
		#Set next pointer of last node to new node	
		temp.next= new_node
		#Set previous pointer of new node to original last node
		new_node.prev= temp	

if __name__=='__main__':

	dllist= DoublyLinkedList()
	
	dllist.head= Node(0)
	second= Node(2)
	third= Node(4)
	fourth= Node(6)
	
	#Setting the next pointers
	dllist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= None
	
	#Setting the previous pointers
	dllist.head.prev= None
	second.prev= dllist.head
	third.prev= second
	fourth.prev= third
	
	print ("Original list")
	dllist.printForward()
	print ("Adding a node at the end of the List with data 8")
	dllist.insertEnd(8)
	dllist.printForward()
	print ("Printing the list in backward direction")
	dllist.printBackward()
