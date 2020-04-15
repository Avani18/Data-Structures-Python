#Implementing Queues using queue library

#Import the module
from queue import Queue

#Initialise a queue
q = Queue(maxsize = 3)

#Print the size of the queue
print ("Size: ",q.qsize())

#Add elements to the queue
q.put(2)
q.put(4)
q.put(6)

#Print if queue is full or not
print ("Full: ", q.full())

#Dequeue elements from the queue
print ("Elements dequeued from the queue")
print (q.get())
print (q.get())
print (q.get())

#Print if queue is empty or not
print ("Empty: ", q.empty())

#Add an element to the queue
q.put(8)
#Print the size of the queue
print ("Size: ",q.qsize())
#Print if queue is empty or not
print ("Empty: ", q.empty())
#Print if queue is full or not
print ("Full: ", q.full())
