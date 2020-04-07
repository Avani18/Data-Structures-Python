#Find the node at the middle of the Linked List

#Class for making nodes
class Node:

	def __init__(self, data):
		self.data= data
		self.next= None
		
#Class for making a Linked List		
class LinkedList:

	def __init__(self):
		self.head= None

#Function to print the Linked List		
	def printList(self):
		temp= self.head
		
		#Check if Linked List is empty
		if (temp==None):
			print ("Linked List is empty")
			return 
			
		while (temp):
			print (temp.data, end='\t')
			temp= temp.next
		print ('')
	
#Function to find the middle node of the Linked List by method 1
#In this function, we will use 2 pointers. One pointer will move 2 nodes at a time and the other one will move 1 node at a time. When the faster pointer reaches the end of the list, the other pointer reaches the middle of the list and we can then return its value.
	def middleNode1(self):

		#First pointer which will have the value of middle node
		temp1= self.head
		#Fast pointer to move 2 nodes at a time
		temp2= self.head
		
		#Iterate the whole List till the fast pointer reached the end of the List
		while((temp2 is not None) and (temp2.next is not None)):
			#Increment the first pointer
			temp1= temp1.next
			#Increment the second pointer
			temp2= temp2.next.next
			
		#Return the required data	
		return temp1.data	

#Function to find the middle node of the Linked List by method 2
#In this function, we will have a counter whose value is incremented at each step. The pointer of mid node will move only when value of counter is odd. Therefore, by the end of the list, the mid node would have reached the middle of the List.		
	def middleNode2(self):
	
		#Set counter to 0
		counter=0
		#Pointer to iterate the List
		temp= self.head	
		#Pointer to reach the mid of the List
		mid= self.head
		
		#Iterate the Linked List
		while(temp):
			#Check if counter is odd
			if (counter%2!=0):
				#Move the mid pointer
				mid= mid.next
			#Increment the counter
			counter+=1
			#Move the temp node to iterate
			temp= temp.next
			
		#Return the required data
		return mid.data
		
if __name__=='__main__':
	
	llist= LinkedList()
	
	llist.head= Node(2)
	second= Node(4)
	third= Node(6)
	fourth= Node(8)
	fifth= Node(10)
	
	llist.head.next= second
	second.next= third
	third.next= fourth
	fourth.next= fifth
	#fifth.next= Node(12)
	
	print ("Original list is ")
	llist.printList()
	print ("Middle node of list from method 1 is ", llist.middleNode1())
	print ("Middle node of list from method 2 is ", llist.middleNode2())
