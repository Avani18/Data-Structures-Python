#Removing the first node of a Linked List 

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
		
#Function to remove the first node of the List			
	def removeFirstNode(self):
		#Store the original head node in a temporary node to free the memory later
		temp= self.head
		#Set the new head of the Linked List
		self.head= self.head.next
		#Free the memory of the old one
		temp= None
		
if __name__=='__main__':
	
	llist= LinkedList()
	
	llist.head= Node(0)
	second= Node(2)
	third= Node(4)
	fourth= Node(6)
	
	llist.head.next= second
	second.next= third
	third.next= fourth
	
	print ("Original list is ")
	llist.printList()
	print ("Removing first node")
	llist.removeFirstNode()
	print ("First node removed")
	llist.printList()
