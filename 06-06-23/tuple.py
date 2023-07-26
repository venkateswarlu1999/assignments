# write a program to take tuple of numbers from your key board and print sum , average
# numbers=int(input('enter range of tuple: '))
# sum=0
# t=tuple(range(1,numbers))
# print(t)
# for i in t:
#     sum+=i
# print('sum of tuple is: ',sum)
# print('avarage of tuple is: ',sum/len(t))


# list=[]
# n=int(input('enter the range of ur entering numbers: '))
# for i in range(n):
#     ete=int(input())
#     list.append(ete)
# t=tuple(list)
# print(t)
# count=0
# for i in t:
#     count+=i
# print('some of the tuple is: ',count)
# print('the avarage of the tuple is: ',count/len(t))




# 1. Write a Python program to create a tuple.
#we create a tuple in differnt ways these are some of that
# t=()
# print(type(t))
# t=10,
# print(type(t))
# t=10,20,30
# print(type(t))
# t=tuple(range(7))
# print(type(t))
# t=(10,20,30)
# print(type(t))
# 2. Write a Python program to create a tuple with different data types.
# s='23,24,34,7'
# l=s.split(',')
# l1=[]
# for i in l:
#     if i.isdigit():
#         l1.append(int(i))
# print(l1)
# t=tuple(l1)
# print(t)

# l=[10,20,40]
# t=tuple(l)
# print(t)

# s={10,10,20,40}
# print(s)
# print(tuple(s))

# d={1:10,2:20,3:30}
# print(d.values())
# print(tuple(d.values()))




# 3. Write a Python program to create a tuple of numbers and print one item.
# t=((1,2,3),(4,5,6),(7,8,9))
# print(t[0])
# print(t[0][0])
# print(t[0][1])
# print(t[0][2])

# print(t[1])
# print(t[1][0])
# print(t[1][1])
# print(t[1][2])

# print(t[2])
# print(t[2][0])
# print(t[2][1])
# print(t[2][2])



# 4. Write a Python program to unpack a tuple into several variables.
# t=(2,3,4)
# a,b,c=t
# print('a:',a,'b:',b,'c:',c)



# 5. Write a Python program to add an item to a tuple.
# t=(10,20,30)
# print(t+(100,))

# 6. Write a Python program to convert a tuple to a string.

# 7. Write a Python program to get the 4th element from the last element of a tuple.


# 8. Write a Python program to create the colon of a tuple.


# 9. Write a Python program to find repeated items in a tuple.


# 10. Write a Python program to check whether an element exists within a tuple.



# 11. Write a Python program to convert a list to a tuple.



# 12. Write a Python program to remove an item from a tuple.



# 13. Write a Python program to slice a tuple.



# 14. Write a Python program to find the index of an item in a tuple.



# 15. Write a Python program to find the length of a tuple.



# 16. Write a Python program to convert a tuple to a dictionary.



# 17. Write a Python program to unzip a list of tuples into individual lists.



# 18. Write a Python program to reverse a tuple.



# 19. Write a Python program to convert a list of tuples into a dictionary.



# 20. Write a Python program to print a tuple with string formatting.
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)



# 21. Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]



# 22. Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']



# 23. Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


# 24. Write a Python program to count the elements in a list until an element is a tuple.


# 25. Write a Python program to convert a given string list to a tuple.
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
# <class 'tuple'>


# 26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648


# 27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]


# 28. Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))


# 29. Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570


# 30. Write a Python program to check if a specified element appears in a tuple of tuples.
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
# False


# 31. Write a Python program to compute the element-wise sum of given tuples.
# Original lists:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)


# 32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
# Original list of tuples:
# [(1, 2), (2, 3), (3, 4)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [3, 5, 7]
# Original list of tuples:
# [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [9, -1, 7, 8]


# 33. Write a Python program to convert a given list of tuples to a list of lists.
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

# from prettytable import PrettyTabble
# data_dict={'sno':1,'sname':'venky','marks':75}


# table= PrettyTabble()
# table.filed_names =list(data_dict.key())

# table.add_row(list(data_dict.values()))
# print(table)
# r=int(input('enter how many fileds do u want: '))
# data={}
# for i in range(r):
#     dict_keys=input('Enter dict key values: ')
#     dict_values=input('Enter dict values: ')
#     data[dict_keys]=dict_values
# print(data)

# num_entries = int(input("Enter the number of entries: "))

# data_dict = {}

# for i in range(num_entries):
#     key = input("Enter the key: ")
#     value = input("Enter the value: ")
#     data_dict[key] = value

# max_key_length = max(len(key) for key in data_dict.keys())
# max_value_length = max(len(str(value)) for value in data_dict.values())

# table_header = f"Sno. {'Sname':<{max_key_length}} {'Marks':<{max_value_length}}"
# print(table_header)

# for sno, (key, value) in enumerate(data_dict.items(), start=1):
#     table_row = f"{sno:<4} {value:<{max_value_length}}"
#     print(table_row)


