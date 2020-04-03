#Delete the whole Linked List 


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
		
		#Check if Linked List is empty
		if (temp==None):
			print ("Linked List is empty")
			return 
			
		while (temp):
			print (temp.data, end='\t')
			temp= temp.next
		print ('')
	
#Function to delete the List
	def deleteList(self):
	
		#Check if Linked List is already empty
		if (self.head==None):
			print ("List is already empty")
			return
		
		#Iterate every node till the end and delete it 	 
		while (self.head):
			#Store the next node in this
			store_next= self.head.next
			#Free the memory of the current node
			self.head= None
			#Shift the head to the next node
			self.head= store_next
		
if __name__=='__main__':
	
	llist= LinkedList()
	
	llist.head= Node(2)
	second= Node(4)
	third= Node(6)
	fourth= Node(8)
	
	llist.head.next= second
	second.next= third
	third.next= fourth
	
	print ("Original list is ")
	llist.printList()
	print ("Deleting the whole Linked List")
	llist.deleteList()
	print ("List deleted")
	llist.printList()
