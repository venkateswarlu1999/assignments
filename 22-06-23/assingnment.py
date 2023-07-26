# 1. Calculate the sum of all numbers from 1 to a given number.
# n=eval(input('Enter your number: '))
# total = 0
# for i in range(1, n+1):
#     total += i
# print(total)


# 2. Write a program to print multiplication table of a given number.
# number = int(input("Enter a number: "))
# print("Multiplication table of : ",number)
# for i in range(1, 11):
#     product = number * i
#     print("{} x {} = {}".format(number,i,product))

# 3: Display numbers from a list using loop.
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)

# 4: Count the total number of digits in a number.
# number = int(input("Enter a number: "))
# count = 0
# while number != 0:
#     number //= 10
#     count += 1
# print("Total number of digits:", count)
# ----------------------------------------
# number = input("Enter a number: ")
# print(len(number))

# 7: Print list in reverse order using a loop.
# list = [1, 2, 3, 4, 5]
# for i in range(len(list) - 1, -1, -1):
#     print(list[i])

# 8: Display numbers from -10 to -1 using for loop.
# for i in range(-10, 0):
#     print(i)

# 9: Use else block to display a message Done after successful execution of for loop.
# number = int(input("Enter a range of numbers u can check it devided by 10 or not: "))
# for num in  range(1,number+1):
#     if num == 0:
#         print("Cannot divide by zero!")
#         break
#     result = 10 / num
#     print("The result is: ",result)
# else:
#     print("Done")

# 10: Write a program to display all prime numbers within a range.
# start = int(input("Enter the start range: "))
# end = int(input("Enter the end range: "))
# print("Prime numbers between", start, "and", end, "are:")
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# 11: Display Fibonacci series up to 10 terms.
# r = int(input("Enter the terms you want print fibonacci series: "))
# a = 0
# b = 1
# for i in range(r):
#     c = a + b
#     print(c, end=' ')
#     a = b
#     b = c

# 12: Find the factorial of a given number.
# number = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
#     print(factorial)
# print("The factorial of", number, "is", factorial)
# n=int(input('enter a number:'))
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# a=fact(n)
# print(a)
# 13: Reverse a given integer number.
# number =input("Enter a number: ")
# reversed_str = number[::-1]
# reversed_number = int(reversed_str)
# print(reversed_number)

# 14: Use a loop to display elements from a given list present at odd index positions.
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(1, len(list), 2):
#     print(list[i])


# 15: Calculate the cube of all numbers from 1 to a given number.
# N = int(input("Enter a range of numbers: "))
# for num in range(1, N+1):
#     cube = num ** 3
#     print("The cube of {} is {}".format(num,cube))

# 16: Find the sum of the series upto n terms.
# n = int(input("Enter the range (number of terms): "))
# sum_of_series = 0
# for i in range(n):
#     odd_number = 2*i + 1
#     sum_of_series += odd_number
#     print('series of ood numbes is: ',odd_number)

# print("Sum of the series:", sum_of_series)

# 17: Append new string in the middle of a given string.
# Given = "Hello World"
# sub_st = "beautiful "
# midile = len(Given) // 2
# sub_st = Given[:midile] +' '+ sub_st + Given[midile:]
# print(sub_st)

# 18: Arrange string characters such that lowercase letters should come first.
# st =input('Enter any string in both lower and upper: ')
# lower = []
# upper = []

# for char in st:
#     if char.islower():
#         lower.append(char)
#     else:
#         upper.append(char)
# lower.sort()
# upper.sort()
# order_st = ''.join(lower + upper)
# print(order_st)

# 19: Count all letters, digits, and special symbols from a given string.
# st =input('Enter any string in both lower and upper and special char also: ')

# letters = 0
# digits = 0
# special_char = 0

# for char in st:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         special_char += 1
# print("Number of letters:", letters)
# print("Number of digits:", digits)
# print("Number of special symbols:", special_char)

# 20: Find all occurrences of a substring in a given string by ignoring the case.
# st =input('Enter a string: ')
# subst =input('Enter a substring: ')
# occurrences = []
# string = st.lower()
# substring = subst.lower()
# start_index = 0

# while True:
#     index = string.find(substring, start_index)
#     if index == -1:
#         break
#     occurrences.append(index)
#     start_index = index + 1
##############################################
# for i in range(len(st) - len(subst) + 1):
#     if st[i:i + len(substring)] == substring:
#         occurrences.append(i)
# print(occurrences)

# 21: Calculate the sum and average of the digits present in a string.
# st =input('Enter a string with digits also: ')
# sum_digits = 0
# count_digits = 0

# for i in st:
#     if i.isdigit():
#         digit = int(i)
#         sum_digits += digit

#         count_digits += 1
# print(count_digits)
# print(sum_digits)
# average = sum_digits / count_digits
# print("Sum of digits:", sum_digits)
# print("Average of digits:", average)

# 22: Write a program to count occurrences of all characters within a string.
# string = input("Enter a string: ")
# count = {}

# for i in string:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# for i, count in count.items():
#     print("cha:",i,"occurences:",count)

# 23: Reverse a given string.
# st = "Hello, World"
# rst = st.split()
# print(rst)
# re=' '.join(rst[::-1])
# print(re)
# s=''
# for i in st:
#     s=i+s
# print(s)

# 24: Split a string on hyphens.
# n=input('enter a string: ')
# n.split()
# s='_'.join(n)
# print(s)
# 25: Remove empty strings from a list of strings.
# 30: Remove empty strings from the list of strings.
# my_list = ["hello", "", "world", "", "open", "", "AI"]
# my_list = [i for i in my_list if i.isalpha()]
# print(my_list)
# n=input('enter a string: ')
# l=[]
# st=''
# for i in n:
#     l.append(i)
# for j in l:
#     if j.isalpha():
#         st+=j
# print(st)




# 26: Removal all characters from a string except integers.
# st = input('enter a string include digits also: ')
# result = ""
# for i in st:
#     if i.isdigit():
#         result += i
# print(result)

# 27: Reverse a list in Python.
# l = [1, 2, 3, 4, 5]
# l.reverse()
# print(l)
# l = [1, 2, 3, 4, 5]
# rl = l[::-1]
# print(rl)

# 28: Concatenate two lists index-wise.
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# result = []
# for i in range(len(l1)):
#     result.append(str(l1[i]) + str(l2[i]))
# print(result)

# 29: Turn every item of a list into its square.
# l = [1, 2, 3]
# re=[]
# for i in l:
#     re.append(i**2)
# print(re)

# 31: Add new item to list after a specified item.
# list=[]
# a=int(input('enter lenth of your list: '))
# for i in range(a+1):
#     list.append(i)
# print('present list look like: ',list)
# n=int(input("add_after_item list can be modify: "))
# number=int(input('Enter what number you can modify: '))
# list.insert(n+1,number)
# print(list)


# 32: Replace list item with new value if found.
# old=int(input('Enter what number you can modify: '))
# new=int(input('which number can be modifed number: '))
# lst = [1, 2, 3, 4, 5, 2]
# for i in range(len(lst)):
#     if lst[i] == old:
#         lst[i] = new
# print(lst)


# 33: Remove all occurrences of a specific item from a list.
# l = [1, 2, 3, 4, 2, 5, 2]
# print('present list: ',l)
# n=int(input('which number can be removed: '))
# new_lst = []
# for i in l:
#     if i != n:
#         new_lst.append(i)
# print(new_lst)



###########################################################################
# creating a tables
# def multiplication_table(rows, columns):
#     for i in range(1, rows + 1):
#         for j in range(1, columns + 1):
#             value = i * j
#             print("{} * {} = {}".format(i,j,value))
#         print()
# multiplication_table(2, 10)

# Check given number  perfect number or not
# n=int(input('enter a number:'))
# sum=0
# for i in range(1,n):
#     print(i)
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print('perfect number')
# else:
#     print('not perfect number')

# qadraticequation (-b+- square root of (b**2 - 4ac)/2a)
# import cmath
# a=1
# b=5
# c=6
# d=(b**2)-(4*a*c)
# e= (-b+cmath.sqrt(d))/2*a
# e1= (-b-cmath.sqrt(d))/2*a
# print(e)
# print(e1)

# to convert given number decimal to binary,octal and hegxa
# n=int(input('enter a number:'))
# print(bin(n)[2:])
# print(oct(n)[2:])
# print(hex(n)[2:])


# by using bubble short given list in assining order
# l=[23,45,67,12,1,2,40,98]
# def bubbleshort(arry):
#     for i in range(len(arry)):
#         for j in range(0,len(arry)-i-1):
#             if arry[j]>arry[j+1]:
#                 a=arry[j]
#                 arry[j]=arry[j+1]
#                 arry[j+1]=a
# bubbleshort(l)
# print(l)

# l=[23,45,67,12,1,2,40,98]
# b=sorted(l)
# print(b)

# swaping of two numbers without usig temp ver and with temp var
# a=1         
# b=2
# a,b=b,a
# print(a)
# print(b)
# c=a
# a=b
# b=c
# print(a)
# print(b)

# n=int(input('enter a number:'))
# def fib(n):
#     a,b=0,1
#     while a<n:
#         print(a)
#         a,b=b,a+b

# fib(n)

# n=int(input('enter a number:'))
# def fib(n):
#     if n<0:
#         print('incorrect value')
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(n):
#     print(fib(i))