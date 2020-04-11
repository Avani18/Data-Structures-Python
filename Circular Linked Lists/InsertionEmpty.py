#Insertion of node in an empty list

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
		
#Function to add a node to the empty List
#This function takes 1 paramter- the data of the node to be added
	def insertEmpty(self, data):
		self.head= Node(data)
		#Point the next pointer to itself to make it Circular
		self.head.next= self.head	
		
if __name__=='__main__':
	
	cllist= CircularLinkedList()
	
	print ("The list after adding one node is ")
	cllist.insertEmpty(2)
	cllist.printList()
