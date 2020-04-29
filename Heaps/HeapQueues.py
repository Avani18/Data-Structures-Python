#Implementing the basic functions of a min heap using heapq

import heapq

#Initialise a List
myList = [5, 7, 9, 1, 3]

#Convert it to a min heap
heapq.heapify(myList)

#Print the heap
print ("The created heap is: ")
print (list(myList))

#Push an element
heapq.heappush(myList, 4)

#Print the modified heap
print ("The modified heap after push is: ")
print (myList)

#Pop an element
print ("The popped and smallest element is: ", end = ' ')
print (heapq.heappop(myList))

#Initialise 2 same Lists
myList1 = [5, 7, 9, 4, 3]
myList2 = [5, 7, 9, 4, 3]

#Convert them to min heap
heapq.heapify(myList1)
heapq.heapify(myList2)

#Show heappushpop which first pushes an element and then pops from the heap
print ("The popped item using heappushpop() is: ", end = ' ')
print (heapq.heappushpop(myList1, 2))

#Show heapreplace which first pops an element and then pushes the new element
print ("The popped item using heapreplace() is: ", end = ' ')
print (heapq.heapreplace(myList2, 2))

#Initialise a List
myList3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

#Convert it to a min heap
heapq.heapify(myList3)

#Print the 3 largest numbers
print ("The 3 largest numbers in the List are: ", end = ' ')
print (heapq.nlargest(3, myList3))

#Print the 3 smallest numbers
print ("The 3 smallest numbers in the List are: ", end = ' ')
print (heapq.nsmallest(3, myList3))
