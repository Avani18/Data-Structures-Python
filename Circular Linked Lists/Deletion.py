#Deletion of a given data node

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
		
#Function to delete a node with the given data 
#This function takes 1 paramter- the data of the node to be deleted
	def deleteNode(self, data):
	
		#Node to iterate the List
		temp= self.head
		#Node to store the original head or to serve as variable for previous node
		temp1= self.head
		
		#If the List is empty
		if (temp==None):
			print ("List is empty!")
			return
			
		#If the head node contains the data to be deleted	
		if (temp.data== data):
			#Iterate the list to reach the last node
			while(temp.next!= self.head):
				#Move the temp node
				temp= temp.next
			#Set the next pointer of last node to the new head node
			temp.next= self.head.next
			#Change the head node of the list to the second node (next node of original node)
			self.head= temp1.next
			#Delete the original head node
			del temp1
			return
				
		#Delete the node if it is not a head node
		#In this loop, temp1 will serve as variable for previous node
		while (True):
			#Find the required node
			if (temp.data==data):
				#Set the next pointer of the previous node to the next of current node
				temp1.next= temp.next
				#Delete the current node
				del temp1
				return
			#Update the value of previous node
			temp1= temp
			#Move the temp node to next node
			temp= temp.next
			#Check if List iteration has finished
			if (temp==self.head):
				print ("The entered data item does not exist in the List")
				return
		
if __name__=='__main__':
	
	cllist= CircularLinkedList()
	
	cllist.head= Node(2)
	second= Node(4)
	third= Node(5)
	fourth= Node(6)
	fifth= Node(8)
	
	cllist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= fifth
	fifth.next= cllist.head
	
	print ("Original List is ")
	cllist.printList()
	print ("Deleting a node with data 5")
	cllist.deleteNode(5)
	cllist.printList()
