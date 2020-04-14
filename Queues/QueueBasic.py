#Implement Queue from scratch using Lists

#Class for creating queues
class Queue:

#Constructor which takes a parameter capacity for the size of the queue
	def __init__(self, capacity):
		#Initialise the front of the queue and the size of the queue to be 0
		self.front= self.size= 0
		#Initialise the rear of the queue
		self.rear= capacity-1
		#Create a list of Nones with size capacity
		self.Q= [None]*capacity
		#Set the capacity of the queue
		self.capacity= capacity
		
#Function to check if the queue is full or not
	def isFull(self):
		#If size of queue = capacity of queue, it is full
		if (self.size==self.capacity):
			return True
		else:
			return False
			
#Function to check if the queue is empty or not 
	def isEmpty(self):
		#If size of queue is 0, it is empty 
		if (self.size==0):
			return True
		else:
			return False

#Function to insert an element at the rear of the queue		
	def enQueue(self, item):
		#If queue is full, cannot insert an element 
		if (self.isFull()):
			print ("Queue is full!")
			return
		#Move the rear forward, to keep its value from (0 to capacity-1), we take its mod with the capacity
		self.rear= (self.rear + 1)% (self.capacity)
		#Insert element at rear position
		self.Q[self.rear]= item
		#Increment size of the queue
		self.size+=1
		print (str(item)+ " enqueued to queue")

#Function to remove an element from the front of the queue		
	def deQueue(self):
		#Cannot remove element if queue is empty
		if (self.isEmpty()):
			print ("Queue is empty!")
			return
		#Element at the front pointer
		print (str(self.Q[self.front])+ " dequeued from queue")
		#Move the front forward, to keep its value from (0 to capacity-1), we take its mod with the capacity
		self.front= (self.front + 1) % (self.capacity)
		#Decrement size of the queue
		self.size= self.size - 1

#Function to get the front element of the queue	
	def getFront(self):
		#If queue is empty, cannot get front element
		if (self.isEmpty()):
			print ("Queue is empty!")
			return
		
		#Return element at front
		return self.Q[self.front]

#Function to get the rear element of the queue		
	def getRear(self):
		#If queue is empty, cannot get rear element
		if (self.isEmpty()):
			print ("Queue is empty!")
			return
			
		#Return element at rear
		return self.Q[self.rear]
		
if __name__=='__main__':

	#Create a queue
	queue= Queue(10)
	
	#Insert elements in queue
	queue.enQueue(2)
	queue.enQueue(4)		
	queue.enQueue(6)
	queue.enQueue(8)
	queue.enQueue(10)
	
	#Remove element from queue
	queue.deQueue()
	
	#Print the front element
	print ("The front element is "+ str(queue.getFront()))
	#Print the rear element
	print ("The rear element is "+ str(queue.getRear()))		
