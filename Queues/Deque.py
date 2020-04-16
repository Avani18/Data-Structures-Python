#Using deque module of the collections library to implement deque and all its functions

#Import the library
import collections

#Create a deque 
my_deque= collections.deque([1,2,3])

#Add elememt to the right 
my_deque.append(4)
print ("The deque after appending at right is: ")
print (my_deque)

#Add element to the left
my_deque.appendleft(6)
print ("The deque after appending at left is: ")
print (my_deque)

#Remove element from the right
my_deque.pop()
print ("The deque after deleting from right is: ") 
print (my_deque)

#Remove element from the left
my_deque.popleft()
print ("The deque after deleting from left is: ") 
print (my_deque)


#Create another deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4]) 
  
#Print the index of the first occurence of 4 ranging from index 2 to 5 
print ("The number 4 first occurs at a position : "+ str(de.index(4,2,5))) 
  
#Insert element 3 at 4th index 
de.insert(4,3) 
print ("The deque after inserting 3 at 5th position is : ") 
print (de) 
  
#Print the count of occurence of 3
print ("The count of 3 in deque is : " + str(de.count(3))) 
  
#Remove the first occurence of 3
de.remove(3) 
print ("The deque after deleting first occurrence of 3 is : ") 
print (de) 


#Create another deque
de = collections.deque([1, 2, 3,]) 

#Add iterable of 4,5,6 at the right of queue  
de.extend([4,5,6]) 
print ("The deque after extending deque at end is : ") 
print (de) 
  
#Add iterable of 7,8,9 at the left of queue, They will be added as 9,8,7
de.extendleft([7,8,9]) 
print ("The deque after extending deque at beginning is : ") 
print (de) 
  
#Rotate the queue from left by 3 elements, (positive value for right)
de.rotate(-3) 
print ("The deque after rotating deque is : ") 
print (de) 
  
#Reverse the queue
de.reverse()
print ("The deque after reversing deque is : ") 
print (de) 
