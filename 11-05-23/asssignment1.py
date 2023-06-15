
#1.print the largest of the three numbers using only if statement
# num1 = int(input('Enter your first number: '))
# num2 = int(input('Enter your second number: '))
# num3 = int(input('Enter your third number: '))
# if num1 > num2 :
#     if num1 < num2:
#         print('num2 is bigger then num1: num2 = ',num2)
#     else:
#         print('num2 is not bigger then num1: num1 = ',num1)
# elif num2 > num3:
#     if num2 < num3:
#         print('num2 is not bigger then num3: num3 = ',num3)
#     else:
#         print('num2 is bigger then num3: num2 = ',num2)


#2.check whether a person is eligible to vote or not
'''
age=int(input('enter your age: '))
voterage = 18
if age >= voterage:
    print('your aligible for vote: ',age)
elif 0 < age < voterage:
    print('your aligible for vote after ',voterage - age,'years')
elif age <= 0:
    print('your not born at')
else:
    print('you enter wrong info')
'''
#3.check whether a number is even or not
'''
num = int(input('Enter a number: '))
if num%2 == 0:
    print('It is a neven number,the number is: ',num)
else:
    print('It is not a even number,the number is: ',num)
'''
#4.to check given input number is equal to 20,80,500
'''
num = int(input('Enter a number: '))
if num==20 or num==80 or num==500:
    print('Given number is in equal to 20,80,500',num)
else:
    print('Given number is in not equal to 20,80,500',num)
'''
#5.program to check student grade
'''
marks = eval(input('Enter student marks: '))
if marks > 80 and marks <=100:
    print('He got a grade: A marks =',marks)
elif marks >60 and marks <=80:
    print('He got a grade: B marks =',marks)
elif marks >=35 and marks <=60:
    print('He got a grade: C marks =',marks)
elif marks >=0 and marks <35:
    print('He got a filled marks =',marks)
else:
    print('He not attempt the exam')
'''


