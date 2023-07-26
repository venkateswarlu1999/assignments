# Functions Assigments.
# ----------------------

# 1. Write a Python function to find the maximum of three numbers.
# n=int(input('enter your range of list items: '))
# l=[]
# for i in range(n):
#     b=int(input('enter your list iteams: '))
#     l.append(b)
# print('here it is your created list: ',l)
# print('the maximum number of given is: ',max(l))

# 2. Write a Python function to sum all the numbers in a list.
# 	Sample List : (8, 2, 3, 0, 7)
# 	Expected Output : 20

# l=[8,2,3,0,7]
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# 3. Write a Python function to multiply all the numbers in a list.
# 	Sample List : (8, 2, 3, -1, 7)
# 	Expected Output : -336

# l=[8,2,3,-1,7]
# mul=1
# for i in l:
#     mul=mul*i
# print(mul)

# 4. Write a Python program to reverse a string.
# 	Sample String : "1234abcd"
# 	Expected Output : "dcba4321"

# st= "1234abcd"
# new=''
# for i in st:
#     new=''.join(st[::-1])
# print(new)

# 5. Write a Python function to calculate the factorial of a number. 
# The function accepts the number as an argument.

# n=int(input('enter a number it give a factorial: '))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# a=fact(n)
# print(a)

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# 	Sample String : 'The quick Brow Fox'
# 	Expected Output :
# 	No. of Upper case characters : 3
# 	No. of Lower case Characters : 12
 
# st=input('enter a string: ')
# u=0
# l=0
# for i in st:
#     if i.isalpha():
#         if i.isupper():
#             u+=1
#         else:
#             l+=1
# print('no.of upper letters in given st is: ',u)
# print('no.of lower letters in given st is: ',l)

# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# 	Sample List : [1,2,3,3,3,3,4,5]
# 	Unique List : [1, 2, 3, 4, 5]

# l=[1,2,3,3,3,4,5]
# unquielist=list(set(l))
# print('sample list is: ',l)
# print('unique list is: ',unquielist)

# 9. Write a Python program to print the even numbers from a given list.
# 	Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 	Expected Result : [2, 4, 6, 8]

# Sample=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# l=[]
# for i in Sample:
#     if i%2==0:
#         l.append(i)
# print('we can taken sample lis is: ',Sample)
# print('Extract the even numbers list is :',l)

# 10. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# 	Sample Items : green-red-yellow-black-white
# 	Expected Result : black-green-red-white-yellow

# 11. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30
# n=int(input('enter your list range: '))
# l=[]
# for i in range(1,n+1):
#     l.append(i**2)
# print('your required list is created by its squares: ',l) 

# 12. Write a Python program to create any chain of function decorators.

# def dec1(fun):
#     def inner():
#         x=fun()
#         return x*x
#     return inner

# def dec2(fun):
#     def inner():
#         x=fun()
#         return 2*x
#     return inner
# @dec2
# @dec1
# def n():
#     return 10
# print(n()) 

# 13. Write a Python program to access a function inside a function.

# def outer(fun):
#     print('outer function execution')
#     def inner(name):
#         print("inner function execution")
#         fun(name)
#     print('outer function enter into the inner function')
#     return inner
# def w(name):
#     print("hello",name,"morning")

# a=outer(w)
# a('venkat')