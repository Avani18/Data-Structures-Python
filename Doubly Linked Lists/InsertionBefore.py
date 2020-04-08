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
	
	dllist.head= Node(0)
	second= Node(4)
	third= Node(6)
	fourth= Node(10)
	
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
	print ("Adding a node before 1st index node with data 2")
	dllist.insertBeforeIndex(2,1)
	dllist.printForward()
	print ("Adding a node before 'fourth' node with data 8")
	dllist.insertBeforeNode(8, fourth)
	dllist.printForward()
	print ("Printing the list in backward direction")
	dllist.printBackward()
