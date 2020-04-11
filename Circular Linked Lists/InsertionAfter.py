#Insertion of node after a given node

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
	
	cllist.head= Node(2)
	second= Node(4)
	third= Node(6)
	fourth= Node(10)
	fifth= Node(12)
	
	cllist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= fifth
	fifth.next= cllist.head
	
	print ("Original List is ")
	cllist.printList()
	print ("Adding a node after the 2nd index of the List")
	cllist.insertAfter(8,2)
	cllist.printList()
