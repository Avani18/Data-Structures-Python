#Insert a node at the front of the List

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

#Function to insert a node at the front of the List
#This function takes 1 parameter- data of the new node to be added 	
	def insertFront(self, data):
	
		#Store the original head node
		temp= self.head 
		#Assign the new head node with given data
		self.head= Node(data)
		#Set the next pointer of new head to old head
		self.head.next= temp
		#Set previous pointer of new head to None
		self.head.prev= None
		#Set previous pointer of old head to new head
		temp.prev= self.head

if __name__=='__main__':

	dllist= DoublyLinkedList()
	
	dllist.head= Node(2)
	second= Node(4)
	third= Node(6)
	fourth= Node(8)
	fifth= Node(10)
	
	#Setting the next pointers
	dllist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= fifth
	fifth.next= None
	
	#Setting the previous pointers
	dllist.head.prev= None
	second.prev= dllist.head
	third.prev= second
	fourth.prev= third
	fifth.prev= fourth
	
	print ("Original list")
	dllist.printForward()
	print ("Adding a node at the front with data 0")
	dllist.insertFront(0)
	dllist.printForward()
	print ("Printing the list in backward direction")
	dllist.printBackward()
