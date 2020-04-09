#Insert a node before a given node in the List

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
		
#Function to insert a node after a given index in the List
#This function takes 2 parameters- data of the new node to be added and the index of node after which it has to be added	
	def insertAfterIndex(self, data, position):
	
		#Check if List is empty	
		if (self.head== None):
			print ("The List is empty!")
			return 
		
		#Node to iterate the List	
		temp= self.head
		#Create the new node
		new_node= Node(data)
		#Counter to know the index of node
		counter= 0
		
		#Iterating the List
		while (temp):
			#If required node is found
			if (counter==position):
				#Set previous pointer of new node to the current node
				new_node.prev= temp
				#Set next pointer of new node to the next of current node
				new_node.next= temp.next
				#Set next pointer of current node to new node
				temp.next= new_node
				#Check if there is a node after the new node 
				if (new_node.next is not None):
					#Set the previous pointer of new node's next node to the new node
					new_node.next.prev= new_node
				return 

			#Increment counter
			counter+=1
			#Move the temp node
			temp= temp.next	
			
		print ("The given index does not exist in the List")

#Function to insert a node after a given node in the List
#This function takes 2 parameters- data of the new node to be added and the node after which it has to be added		
	def insertAfterNode(self, data, node):
		
		#Check if the given node is empty
		if (node== None):
			print ("The given node does not exist")
			return
		
		#Create the new node
		new_node= Node(data)
		#Set next pointer of new node to next of given node
		new_node.next= node.next
		#Set previous pointer of new node to given node
		new_node.prev= node
		#Set next pointer of given node to new node
		node.next= new_node
		#Check if there is a node after the new node 
		if (new_node.next is not None):
			#Set the previous pointer of new node's next node to the new node
			new_node.next.prev= new_node

#Function to insert a node before a given index in the List
#This function takes 2 parameters- data of the new node to be added and the index of node before which it has to be added	
	def insertBeforeIndex(self, data, position):
	
		#Check if List is empty	
		if (self.head== None):
			print ("The List is empty!")
			return 
		
		#Node to iterate the List	
		temp= self.head
		#Create the new node
		new_node= Node(data)
		#Counter to know the index of node
		counter= 0
		
		#Iterating the List
		while (temp):
			#If required node is found
			if (counter==position):
				#Set next pointer of new node to the current node
				new_node.next= temp
				#Set previous pointer of new node to the previous of current node
				new_node.prev= temp.prev
				#Set previous pointer of current node to new node
				temp.prev= new_node
				#Check if there is a node before the new node 
				if (new_node.prev is not None):
					#Set the next pointer of new node's previous node to the new node
					new_node.prev.next= new_node
				#This means that the new node is also the new head node so we assign it
				else:
					self.head=new_node
				return 

			#Increment counter
			counter+=1
			#Move the temp node
			temp= temp.next	
			
		print ("The given index does not exist in the List")

#Function to insert a node before a given node in the List
#This function takes 2 parameters- data of the new node to be added and the node before which it has to be added		
	def insertBeforeNode(self, data, node):
		
		#Check if the given node is empty
		if (node== None):
			print ("The given node does not exist")
			return
		
		#Create the new node
		new_node= Node(data)
		#Set next pointer of new node to the given node
		new_node.next= node
		#Set previous pointer of new node to previous of given node
		new_node.prev= node.prev
		#Set previous pointer of given node to new node
		node.prev= new_node
		#Check if there is a node before the new node 
		if (new_node.prev is not None):
			#Set the next pointer of new node's previous node to the new node
			new_node.prev.next= new_node	

if __name__=='__main__':

	dllist= DoublyLinkedList()
	
	dllist.head= Node(6)
	
	dllist.insertFront(2)
	dllist.insertBeforeIndex(0,0)
	dllist.insertEnd(8)
	dllist.insertAfterIndex(10,3)
	dllist.insertBeforeIndex(4,2)
	
	print ("Printing the list in forward direction")
	dllist.printForward()
	print ("Printing the list in backward direction")
	dllist.printBackward()
