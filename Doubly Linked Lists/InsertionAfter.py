#Insert a node after a given node in the List

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

if __name__=='__main__':

	dllist= DoublyLinkedList()
	
	dllist.head= Node(0)
	second= Node(2)
	third= Node(4)
	fourth= Node(8)
	
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
	print ("Adding a node after 2nd index node with data 6")
	dllist.insertAfterIndex(6,2)
	dllist.printForward()
	print ("Adding a node after 'fourth' node with data 10")
	dllist.insertAfterNode(10, fourth)
	dllist.printForward()
	print ("Printing the list in backward direction")
	dllist.printBackward()
