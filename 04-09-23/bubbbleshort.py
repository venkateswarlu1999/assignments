# Python implementation of above
# algorithm
# Node class
class Node:
	
	# Constructor to initialize the
	# node object
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to sort a singly
# linked list using insertion
# sort
def insertionSort(start):

	# Initialize sorted linked list
	sorted = None

	# Traverse the given linked list
	# and insert every node to sorted
	current = start
	while (current != None):
	
		# Store next for next iteration
		next = current.next

		# Insert current in sorted
		# linked list
		sorted = sortedInsert(sorted,current)
		# Update current
		current = next
	
	# Update start to point to
	# sorted linked list
	start = sorted
	return start

# Function to insert a new_node in a list.
# Note that this function expects a pointer
# to start as this can modify the head
# of the input linked list (similar to push())
def sortedInsert(start, new_node):
	current = None
	
	# Special case for the head end
	if (start == None or
	(start).data >= new_node.data):
		new_node.next = start
		start = new_node
	
	else:
	
		# Locate the node before the point
		# of insertion
		current = start
		while (current.next != None and
			current.next.data < new_node.data):	
			current = current.next
		
		new_node.next = current.next
		current.next = new_node
		
	return start

# Utility Functions
# Function to print linked list
def printList(head):
	temp = head
	while(temp != None):
		print( temp.data, end = " ")
		temp = temp.next
	
# A utility function to insert a node
# at the beginning of linked list
def push( start, new_data):

	# Allocate node
	new_node = Node(0)

	# Put in the data
	new_node.data = new_data

	# Link the old list of the
	# new node
	new_node.next = (start)

	# Move the head to point to
	# the new node
	(start) = new_node
	return start

# Driver code
a = None
a = push(a, 5)
a = push(a, 20)
a = push(a, 4)
a = push(a, 3)
a = push(a, 30)

print("Linked List before sorting ")
printList(a)

a = insertionSort(a)

print("Linked List after sorting ")
printList(a)
# This code is contributed by Arnab Kundu


# '''
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

#  Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# '''
# def maxSubArraySumAndTheArray(nums):
#     maxSum = -999999999999999999999999999999999
#     maxSubaraay = []
#     l = len(nums)
#     for i in range(l):
#         currentSum = 0
#         currentSubArrau = []

#         for j in range(i,l):

#             currentSum = currentSum + nums[j]
#             currentSubArrau.append(nums[j])

#             if currentSum>maxSum:
#                 maxSum = currentSum
#                 maxSubaraay = currentSubArrau.copy()

#     print(maxSum)
#     print(maxSubaraay)

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# maxSubArraySumAndTheArray(nums)