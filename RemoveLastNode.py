#Removing the last node of a Linked List 

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
			print (temp.data, end='\t')
			temp= temp.next
		print ('')
		
#Function to remove the last node of the List
#This function does not require any parameters			
	def removeLastNode(self):
		#Check if the Linked List is empty
		if (self.head==None):
			print ("Linked List is empty!")
			return 
			
		#Check if the List contains only one node 	
		if (self.head.next==None):
			#Remove that one node
			self.head= None
			return 
			
		#Iterate to find the second last node	
		second_last= self.head
		#This will continue till the second last node is found
		while (second_last.next.next):
			second_last= second_last.next
			
		#Unlink it from the last node after the loop terminates	
		second_last.next= None		
		
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
	print ("Removing last node")
	llist.removeLastNode()
	print ("Last node removed")
	llist.printList()
