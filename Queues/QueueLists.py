#Implementing Queues from Lists

#Initialise a queue
queue = []

#Add elements to the end of the queue
queue.append('a')
queue.append('b')
queue.append('c')

#Print the queue
print ("Initial queue: ")
print (queue)

#Remove elements from the queue
print ("Elements dequeued from queue: ")
print (queue.pop(0))
print (queue.pop(0))
print (queue.pop(0))

#Print the queue
print ("Queue after removing elements")
print (queue)
