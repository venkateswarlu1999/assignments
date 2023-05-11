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
