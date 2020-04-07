#Calculate length of the Linked List

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
	
#Function to calculate the length of the List
	def calcLength(self):

		#To iterate the whole Linked List
		temp= self.head
		#Counter to calculate length
		length= 0
		#Iterate every node till the last node 	 
		while (temp):
			#Increment the counter
			length+=1
			#Move to the next node
			temp= temp.next
		return length
		
if __name__=='__main__':
	
	llist= LinkedList()
	
	llist.head= Node(2)
	second= Node(4)
	third= Node(6)
	fourth= Node(8)
	
	llist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= Node(10)
	
	print ("Original list is ")
	llist.printList()
	print ("Length of list is ", llist.calcLength())
