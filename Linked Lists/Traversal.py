#Traversing and prinitng the nodes sequentially from a given node 

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
		#Iterate nodes through temp
		temp= self.head
		while (temp):
			print (temp.data)
			temp= temp.next
		
if __name__=='__main__':

	llist= LinkedList()
	
	llist.head= Node(1)
	second= Node(2)
	third= Node(3)
	
	llist.head.next= second
	second.next= third
	
	llist.printList()
