#Removing the node at a given position (index) of the Linked List

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
	
#Function to remove the node at given position
#This function takes 1 parameter- position at which the node is to be deleted	
	def removeNodeAtPos(self, position):
	
		#Check if the Linked List is empty
		if (self.head==None):
			print ("The Linked List is empty")
			return 
		
		#Check if the node to be deleted is the first node
		if (position==0):
			temp= self.head
			#Assign the next node to be the new head node
			self.head= self.head.next
			#Free the memory of the original head node
			temp= None
			return
		
		#A counter which will be used for reaching the required position
		position_counter= 1
		#A node which will store the previous node of the node to be deleted
		prev_node= self.head
		#This contains the node to be deleted
		temp= self.head.next
		
		#This loop iterates till the temp node has the node to be deleted by checking position
		while (position_counter!=position):
			#Update the previous node
			prev_node= temp
			#Update the current node
			temp= temp.next
			#Increment the position counter
			position_counter+=1
			#If the last node is crossed and position is still not found, the given position does not exist
			if (temp==None):
				print ("The given position is not present in the Linked List")
				return 
		
		#This is executed after termination of while loop when required node is found
		#Unlink the node to be deleted
		prev_node.next= temp.next
		#Free the memory of the deleted node
		temp= None

if __name__=='__main__':
	
	llist= LinkedList()
	
	llist.head= Node(2)
	second= Node(4)
	third= Node(5)
	fourth= Node(6)
	
	llist.head.next= second
	second.next= third
	third.next= fourth
	
	print ("Original list is ")
	llist.printList()
	print ("Removing node at 2nd position/index")
	llist.removeNodeAtPos(2)
	print ("Node removed")
	llist.printList()
