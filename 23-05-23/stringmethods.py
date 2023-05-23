# 1. input = raju is good boy
# output = boy good is raju 
# using split function
'''
a = 'raju is good boy'
l=a.split()
rl=l[::-1]
rs= " ".join(str(i) for i in rl)
print('model1 output')
print(rs)
'''
'''
a = 'raju is good boy'
l=a.split()
rl=l[::-1]
rs = " ".join(map(str,rl))
print('model2 output')
print(rs)
'''
'''
a = 'raju is good boy'
l=a.split()
rl=l[::-1]
print('model3 output')
for i in rl:
    print(i,end=" ")
'''
'''
a = 'raju is good boy'
l=a.split()
rl=l[::-1]
rs = '{} {} {} {}'.format(*rl)
print('model4 output')
print(rs)
'''

# 2. program to display all the positions of sub string in the given string using while loop
'''
s = input('Enter any string: ')
sub = input('Enter any sub string: ')
positions = []
index = 0
print(len(s))
print(len(sub))
while index<len(s):
    j = s.find(sub,index)
    if j ==-1:
        break
    else:
        positions.append(j)
        index = j+len(sub)
print('given string: ',s)
print('given sub string: ',sub)
print(positions)

'''
# 3. input = ABBCDEFFGHILJK
# output= ABCDEFGHIJK
# using join function
'''
a = 'ABBCDEFFGHILJK'
sa = sorted(a)
da = set(sa)
ca=''.join(da)
print('practice')
print(ca)
ca = ''.join(sorted(set(a)))
print('finall')
print(ca)

'''
