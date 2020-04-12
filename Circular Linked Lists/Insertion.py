#All types of insertion demonstrated

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
				
#Function to add a node at the end of the List
#This function takes 1 paramter- the data of the node to be added
	def insertEnd(self, data):
	
		#Node to iterate the List
		temp= self.head
		#Make a new node
		new_node= Node(data)
		#Reach the last node
		while (temp.next!=self.head):
			temp= temp.next
		#The old last node now points to the new last node
		temp.next= new_node
		#The new last node points to the head of the List
		new_node.next=self.head	
		
#Function to add a node after a given node in the List
#This function takes 2 paramters- the data of the node to be added and index of node after which new node has to be added
	def insertAfter(self, data, position):
	
		#Node to iterate the List
		temp= self.head
		#Make a new node
		new_node= Node(data)
		#Counter to reach the required node
		counter=0
		#Reach the required node
		while (True):
			#If the required node is reached
			if (counter==position):
				#Set the next pointer of the new node
				new_node.next= temp.next
				#Link the new node after the given position
				temp.next= new_node
				return
			#Increment the coounter
			counter+=1
			#Move the temp node
			temp= temp.next
			#If the head node is reached again means that iteration of list has finished
			if (temp==self.head):
				break
		
		print ("The entered index does not exist in the List")	
		
if __name__=='__main__':
	
	cllist= CircularLinkedList()
	
	cllist.insertEmpty(2)
	cllist.insertFront(0)
	cllist.insertEnd(6)
	cllist.insertAfter(4,1)
	cllist.insertEnd(10)
	cllist.insertAfter(12,4)
	cllist.insertAfter(8,3)
	
	print ("The List is ")
	cllist.printList()
