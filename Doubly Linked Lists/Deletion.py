#Delete a given node from the List

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

#Function to delete a node at a given index in the List
#This function takes 1 parameter- index of node which has to be deleted	
	def deleteIndex(self, position):
	
		#Check if List is empty	
		if (self.head== None):
			print ("The List is empty!")
			return 
		
		#Node to iterate the List
		temp= self.head
		
		#If node to be deleted is head node
		if (position==0):
			#Set the new head
			self.head= temp.next
			#Delete the node
			del temp
			#Set the previous pointer of new head
			self.head.prev= None
			return
		
		#Counter to know the index of node
		counter= 0
		
		#Iterating the List
		while (temp):
			#If required node is found and it is not the last node
			if ((counter==position) and (temp.next is not None)):
				#Set the next pointer of previous node to next of current node
				temp.prev.next= temp.next
				#Set the previous pointer of next node to previous of current node
				temp.next.prev= temp.prev
				#Delete the node
				del temp
				return
			
			#If required node is found and it is the last node
			if ((counter==position) and (temp.next is None)):
				#Set the next pointer of previous node to None
				temp.prev.next= None
				#Delete the node
				del temp
				return

			#Increment counter
			counter+=1
			#Move the temp node
			temp= temp.next	
			
		print ("The given index does not exist in the List")

#Function to delete a node given 
#This function takes 1 parameters- node to be deleted	
	def deleteNode(self, node):
		
		#Check if the given node is empty
		if (node== None):
			print ("The given node does not exist")
			return
			
		#If node to be deleted is head node
		if (node==self.head):
			#Set the new head
			self.head= node.next
			return
		
		#If the node is not the last node
		if (node.next is not None):
			#Set the next pointer of previous node to next of given node
			node.prev.next= node.next
			#Set the previous pointer of next node to previous of given node
			node.next.prev= node.prev
			#Delete the node
			del node
			return
		
		#It is the last node
		#Set the next pointer of previous node to None
		node.prev.next= None
		#Delete the node
		del node

if __name__=='__main__':

	dllist= DoublyLinkedList()
	
	dllist.head= Node(0)
	second= Node(1)
	third= Node(2)
	fourth= Node(3)
	
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
	print ("Deleting the node at 1st index")
	dllist.deleteIndex(1)
	dllist.printForward()
	print ("Deleting the 'fourth' node")
	dllist.deleteNode(fourth)
	dllist.printForward()
	print ("Printing the list in backward direction")
	dllist.printBackward()
