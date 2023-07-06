# creating a tables
# def multiplication_table(rows, columns):
#     for i in range(1, rows + 1):
#         for j in range(1, columns + 1):
#             value = i * j
#             print("{} * {} = {}".format(i,j,value))
#         print()
# multiplication_table(2, 10)

# creating calculations
# A=int(input('Enter first integer value: '))
# B=int(input('Enter second integer value: '))
# def calculation(a,b):
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul
# r=calculation(A,B)
# for i in r:
#     print(i)

# A=input('Enter your name: ')
# B=int(input('Enter tour age: '))
# def info(name,age):
#     if age>=18:
#         print('{} your age is {} ur eligible for vote'.format(name,age))
#     elif age>100:
#         print('{} your age is {} its out of range age'.format(name,age))
#     elif 1<=age<18:
#         print('{} your age is {} ur not eligible for vote'.format(name,age))
#     else:
#         print('{} your age is {} ur not birth at time'.format(name,age))
# info(A,B)

# def pattern(row,column):
#     for i in range(1,row+1):
#         for j in range(1,column+1):
#             print((column+1)-i,end=' ')
#         print()
# pattern(5,5)


# A=int(input('Enterur range of ur pattern: '))
# def diamond_pattern(rows):
#     for i in range(1, rows + 1):
#         print(" " * (rows - i), end="")
#         print("*" * (2 * i - 1))
#     for i in range(rows - 1, 0, -1):
#         print(" " * (rows - i), end="")
#         print("*" * (2 * i - 1))
# diamond_pattern(A)



# def pattern(n):
#     for i in range(1,n+1):
#         print(" " * (n - i), end="")
#         print("*" * (2 * i - 1))
        
# pattern(5)


# def info(name,age,add):
#     print('Haii my name is {} and iam {} years old.iam from {}'.format(name,age,add))
#     print('Haii my name is ',name,'iam',age,'years old .iam from',add)
#     print('Haii my name is ',name,'iam',age,'years old .iam from',add)
#     print('Haii my name is ',name,'iam',age,'years old .iam from',add)

# info()
# info('venkat')
# info(name='venkat',add='hyd',age=23)
