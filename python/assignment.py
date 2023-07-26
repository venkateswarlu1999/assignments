# age=int(input('enter your age: '))
# voterage = 18
# if age >= voterage:
#     print('your aligible for vote: ',age)
# elif 0 < age < voterage:
#     print('your aligible for vote after ',voterage - age,'years')
# elif age <= 0:
#     print('your not born at')
# else:
#     print('you enter wrong info')


# def feb(n):
#     l=[0,1]
#     for i in range(2,n):
#         next=l[i-1]+l[i-2]
#         l.append(next)
#     return l
# n=int(input('enter the no.of feb series: '))
# febseries=feb(n)
# print(febseries)

# a=0
# b=1

# for i in range(1,6):
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c

# k=[1,2,3,4]
# v=['v','s','r','j']
# d={}
# for i in range(len(k)):
#    d[k[i]]=v[i]
# print(d) 

# for num in range(1,11):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# n=4
# matrix=[]
# for i in range(n):
#     row=[]
#     for j in range(n):
#         row.append(i*n+j+1)
#     matrix.append(row)
# print(matrix)