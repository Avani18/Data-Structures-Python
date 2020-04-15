#Implementing Queues using Linked Lists

#Class for creating nodes 
class Node:
	
#Constructor
	def __init__(self, data):
		self.data = data
		self.next = None

#Class for creating queues		
class Queue:
	
#Constructor
	def __init__(self):
		#Set the front and the rear pointer to None
		self.front = self.rear = None
	
#Function to check if the queue is empty
	def isEmpty(self):
		#Returns true if the front is None
		return self.front == None
		
#Function to print the queue
	def printQueue(self):
		#Check if the queue is empty
		if (self.isEmpty()):
			print ("Queue is empty!")
			return
			
		#Node to iterate the queue
		temp = self.front
		#Iterate the whole queue
		while (temp):
			#Print the data
			print (temp.data, end = ' ')
			#Move the node forward
			temp = temp.next
		print ('')

#Function to insert an element	
	def enQueue(self, data):
		#Create a new node
		new_node = Node(data)
		
		#If the Queue is empty
		if (self.rear == None):
			#Set both the front and rear pointer to the first node
			self.front = self.rear = new_node
			return
			
		#Set the next pointer to original rear node to new node
		self.rear.next = new_node
		#Set the new node to be the new rear node
		self.rear = new_node

#Function to remove an element 
	def deQueue(self):
		#Check if the queue is empty
		if (self.isEmpty()):
			print ("Queue is already empty!")
			return
			
		#Node at front to be deleted
		temp = self.front 
		#Set the next node as the new front node 
		self.front = temp.next
		
		#If the queue is now empty
		if (self.front == None):
			#Rear should also be None
			self.rear = None
			
		#Return the removed element
		return temp.data
		
if __name__ == '__main__':

	queue = Queue()
	queue.enQueue(2)
	queue.printQueue()
	queue.enQueue(4)
	queue.printQueue()
	queue.deQueue()
	queue.printQueue()
	queue.enQueue(6)
	queue.printQueue()
	queue.enQueue(8)
	queue.printQueue()
	queue.deQueue()
	queue.printQueue()
	print ("Queue front " + str(queue.front.data))
	print ("Queue rear " + str(queue.rear.data))
