#Implementing Queues using deque

#Importing the module
from collections import deque

#Initialise a queue
q = deque()

#Add elements to queue
q.append(2)
q.append(4)
q.append(6)

#Print the queue
print ("Initial queue")
print (q)

#Remove elements form the queue
print ("Elements dequeued from the queue")
print (q.popleft())
print (q.popleft())
print (q.popleft())

#Print the queue
print ("Queue after removing elements")
print (q)
