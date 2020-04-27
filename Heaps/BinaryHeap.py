#Implementation of basic functions of a Binary Heap using 3 functions from heapq

#Using heappush, heappop, heapify from this
import heapq

#Class to create a new heap
class MinHeap:
	
	#Initialise the heap
	def __init__(self):
		self.heap = []
		
#Function to return the index of parent of ith node 
	def parent(self, i):
		return int((i-1)/2)
	
#Function to insert a new data element in the heap	
	def insertKey(self, data):
		heapq.heappush(self.heap, data)
		
#Function to change the value at ith node to new value (new value < ith)
	def decreaseKey(self, i, new_val):
		#Change the value
		self.heap[i] = new_val
		#If the new value of node becomes less than the parent, swap the values
		while (i != 0 and (self.heap[self.parent(i)] > self.heap[i])):
			self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])
	
#Function to remove the minimum element (root node)	
	def extractMin(self):
		return heapq.heappop(self.heap)
		
#Function to delete a node at ith position
	def deleteKey(self, i):
		#Set that node to value negative infinity
		self.decreaseKey(i, float("-inf"))
		#Pop the heap
		self.extractMin()

#Function to get the minimum element from the heap		
	def getMin(self):
		return self.heap[0]
		
heap = MinHeap()

heap.insertKey(3) 
heap.insertKey(2) 
heap.deleteKey(1) 
heap.insertKey(15) 
heap.insertKey(5) 
heap.insertKey(4) 
heap.insertKey(45) 
  
print ("Minimum value node removed is: ", heap.extractMin()) 
print ("Minimum value in the heap is: ", heap.getMin()) 
heap.decreaseKey(2, 1) 
print ("Minimum value in the heap after decreaseKey() is: ", heap.getMin())
