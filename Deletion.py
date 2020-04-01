#Deleting the first occurence of a node in the Linked List  

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
			print (temp.data)
			temp= temp.next
			
#Function to delete the first occurence of a node in the Linked List 
#This function takes 1 parameter- the data of the node that has to be deleted		
	def delete(self, del_data):
		
		#Initialise a temp node to iterate the List
		temp= self.head
		
		#Check if the head node has the data to be deleted 
		if ((temp is not None) and (temp.data==del_data)):
			#Assign the next node as the new head node
			self.head= temp.next
			#Free the memory of the deleted node
			temp= None
			return 
		
		#Iterate the Linked List till the node with given data is found or till it reaches the end of the List
		while ((temp is not None) and (temp.data!=del_data)):
			#Store the previous node in prev
			prev= temp
			#Move to the next for iteration
			temp= temp.next
			
		#If the loop terminates because of this, this means that the given data node is not present in the list
		if (temp==None):
			print ("The node is not present in the Linked List")
			return 
		
		#If the loop terminates after given data is found, assign the pointer of previous node to link to the next node of the node to be deleted	
		prev.next= temp.next 
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
	
	print ("Original list: ")
	llist.printList()
	print ("Deleting third node")
	llist.delete(5)
	print ("Node deleted")
	llist.printList()
