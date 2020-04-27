#Implementation of heapify function (max heap) from basic

#Function to heapify a given array
#It takes 3 parameters- array consisting of elements of heap, n is the size of the heap, i is the index of root of the heap in the array
def heapify(arr, n, i):
	
	#Largest element index in array 
	largest = i
	#Index of left child
	left_child = 2 * i + 1
	#Index of right child 
	right_child = 2 * i + 2
	
	#If the left child is larger than the root 
	if(left_child < n and arr[left_child] > arr[largest]):
		#Modify the value of largest
		largest = left_child
		
	#If the right child is greater than the root
	if(right_child < n and arr[right_child] > arr[largest]):
		#Modiy the value of largest
		largest = right_child
		
	#If the largest is not the root of heap
	if(largest != i):
		#Swap their values 
		arr[i], arr[largest] = (arr[largest], arr[i])
		
		#Recursively heapify the sub tree
		heapify(arr, n, largest)
		
#Function to build a max heap 
#It takes 2 paramters- array consisting of the elements of heap, n is the size of heap 		
def buildHeap(arr, n):
	
	#Initialise the start index
	startIndex = int((n / 2)) - 1
	#Perform reverse level order traversal from last non-leaf node
	for i in range(startIndex, -1, -1):
		#Heapify each node
		heapify(arr, n, i)
		
		
arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
n = len(arr)
buildHeap(arr, n)
print ("The modified heap is: ")
print (arr)
