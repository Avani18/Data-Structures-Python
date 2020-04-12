#Insertion of node at the end of a list

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
		
if __name__=='__main__':
	
	cllist= CircularLinkedList()
	
	cllist.head= Node(2)
	second= Node(4)
	third= Node(6)
	fourth= Node(8)
	fifth= Node(10)
	
	cllist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= fifth
	fifth.next= cllist.head
	
	print ("Original List is ")
	cllist.printList()
	print ("Adding a node at the end of the List")
	cllist.insertEnd(12)
	cllist.printList()
