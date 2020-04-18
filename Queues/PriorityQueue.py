#Implementing Priority Queue from scratch using Lists

#Class for creating priority queues with the priority being their value
class PriorityQueue:

#Constructor
	def __init__(self):
		#Initialise the queue
		self.queue = []

#Return the string version of the object		
	def __str__(self):
		#A string of all elements of the queue
		return ' '.join([str(i) for i in self.queue])
		
#Function to check if the queue is empty
	def isEmpty(self):
		#If length of queue is empty, return True else False
		return len(self.queue) == []
		
#Function to insert/append an element at the rear of a queue
	def insert(self, data):
		#Append the data to the queue
		self.queue.append(data)
		
#Funtion to remove an element from the queue based on priority 
	def delete(self):
		try:
			#Set the index of the maximum element to 0
			max= 0
			#Iterate the whole queue
			for i in range(len(self.queue)):
				#Check for the max element in the whole queue
				if (self.queue[i] > self.queue[max]):
					#Update the value of max
					max = i
			#Get the maximum element which has to be removed
			item = self.queue[max]
			#Delete the maximum element
			del self.queue[max]
			#Return its value
			return item
		except IndexError:
			print()
			exit()
			
if __name__=='__main__':

	#Create a priority queue
	pQueue= PriorityQueue()
	
	#Insert values in the priority queue
	pQueue.insert(2)
	pQueue.insert(4)
	pQueue.insert(6)
	pQueue.insert(0)
	
	#Print the priority queue
	print (pQueue)
	
	#Remove all the elements from the priority queue
	while not pQueue.isEmpty(): 
		print(pQueue.delete())  
