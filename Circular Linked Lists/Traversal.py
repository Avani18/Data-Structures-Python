#Traversal of Circular Linked List

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
		
		#Check if Linked List is empty
		if (temp==None):
			print ("Circular Linked List is empty")
			return 
		
		#Iterate till termination condition is found
		while (True):
			#Print node data
			print (temp.data, end='\t')
			#Move to next node
			temp= temp.next
			#Check if head node is reached
			if(temp==self.head):
				print (temp.data, end='\t')
				break
		print ('')	
		
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
	
	print ("The list is ")
	cllist.printList()
