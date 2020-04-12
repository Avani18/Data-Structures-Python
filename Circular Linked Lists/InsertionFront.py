#Insertion of node at the beginning of a list

#Class for making nodes
class Node:

	def __init__(self, data):
		self.data= data
		self.next= None
		
#Class for making a Circular Linked List		
class CircularLinkedList:

	def __init__(self):
		self.head= None

#Function to print the Circular Linked List			
	def printList(self):
		temp= self.head
		
		if (temp==None):
			print ("Circular Linked List is empty")
			return 
		
		while (True):
			print (temp.data, end='\t')
			temp= temp.next
			if(temp==self.head):
				print (temp.data, end='\t')
				break
		print ('')	
		
#Function to add a node at the beginning of the List
#This function takes 1 paramter- the data of the node to be added
	def insertFront(self, data):
	
		#Node to iterate the List
		temp= self.head
		#Node to store the original head
		temp1= self.head
		#Update the head node of the list
		self.head= Node(data)
		#Make the new head point to the old head node
		self.head.next= temp1
		
		#Make the last node point to the new head
		#Iterate this till the last node is reached
		while (temp.next!=temp1):
			temp= temp.next
		#The last node points to the new head now
		temp.next= self.head
		
if __name__=='__main__':
	
	cllist= CircularLinkedList()
	
	cllist.head= Node(2)
	second= Node(4)
	third= Node(6)
	fourth= Node(8)
	fifth= Node(10)
	
	cllist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= fifth
	fifth.next= cllist.head
	
	print ("Original List is ")
	cllist.printList()
	print ("Adding a node at the beginning of the List")
	cllist.insertFront(0)
	cllist.printList()
