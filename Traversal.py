#Traversal of Doubly Linked List in both forward and backward direction

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
		
		#Check if the List is empty
		if (self.head==None):
			print ("The List is empty!")
			return
		
		#Node to iterate the List
		temp= self.head	
		while(temp):
			#Print the data
			print (temp.data, end='\t')
			#Move the temp node
			temp= temp.next
		print ('')	
	
#Function to print the List in backward direction
	def printBackward(self):
	
		#Check if the List is empty
		if (self.head==None):
			print ("The List is empty!")
			return
			
		#Node to iterate the List	
		temp= self.head
		#Reach the last node to print backwardly
		while(temp.next!=None):
			temp= temp.next
			
		#Iterate from the end of the List to print data
		while(temp):
			print (temp.data, end='\t')
			#Move the temp node to previous node
			temp= temp.prev
		print ('')

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
	
	print ("Printing the list in forward direction")
	dllist.printForward()
	print ("Printing the list in backward direction")
	dllist.printBackward()
