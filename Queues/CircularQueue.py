#Implementing Circular Queues using Lists

#Class for Circular Queue
class CircularQueue:
	
#Constructor
	def __init__(self,size):
		self.size= size
		#Initialise the queue with given size
		self.queue = [None for i in range(size)]
		#Set front and rear pointers to -1
		self.front = self.rear = -1

#Function to insert an element at the end of the queue		
	def enQueue(self, data):
		#Check if queue is full 
		if (((self.rear + 1) % self.size) == self.front):
			print ("Queue is full!")
		#Check if queue is empty
		elif (self.front==-1):
			#Move front pointer to 0
			self.front= 0
			#Move rear pointer to 0
			self.rear= 0
			#Add the data element
			self.queue[self.rear] = data
		else:
			#Move the rear pointer forward
			self.rear = (self.rear + 1) % self.size
			#Add the data element
			self.queue[self.rear] = data

#Function to remove an element from the front of the queue 			
	def deQueue(self):
		#If queue is empty
		if (self.front == -1):
			print ("Queue is empty!")
		#If queue has only one element
		elif (self.front == self.rear):
			#Get element at the front
			temp = self.queue[self.front]
			#Move front backward
			self.front = -1
			#Move rear backward
			self.rear = -1
			#Return the element
			return temp
		else:
			#Get the element at front
			temp= self.queue[self.front]
			#Move the front pointer forward
			self.front= (self.front + 1) % self.size
			#Return the element
			return temp
			
#Function to print the circular queue 
	def display(self):
		#If queue is empty
		if (self.front == -1):
			print ("Queue is empty!")
		#If queue is full
		elif (self.rear >= self.front):
			print ("Elements in the Circular Queue are: ", end= ' ')
			#Iterate the whole queue
			for i in range(self.front, self.rear + 1):
				print (self.queue[i], end=' ')
			print ()
		else:
			print ("Elements in Circular Queue are: ", end= ' ')
			#Iterate the queue 
			for i in range(self.front, self.size):
				print (self.queue[i], end= ' ')
			for i in range(0, self.rear + 1):
				print (self.queue[i], end= ' ')
			print ()
		
		#Check if queue is full
		if ((self.rear + 1) % self.size == self.front):
			print ("Queue is full!")

#Create a Circular Queue			
cq = CircularQueue(5)

#Add elements to the queue
cq.enQueue(14)
cq.enQueue(22)
cq.enQueue(13)
cq.enQueue(-6)

#Display the queue
cq.display()

#Delete 2 elements
print ("Deleted value = ", cq.deQueue())
print ("Deleted value = ", cq.deQueue())

#Display the queue
cq.display()

#Add elements to the queue 
cq.enQueue(9)
cq.enQueue(20)
cq.enQueue(5)

#Display the queue 
cq.display()
