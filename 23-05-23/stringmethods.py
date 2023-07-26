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
print('the given sub string found at: 'positions)

'''
'''
s = input('Enter any string: ')
sub = input('Enter any sub string: ')
index=s.find(sub,0,len(s))

if index >=0:
    print('your sub string found at index of: ',index)
else:
    print('your sub string is not found')

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
'''
l=[10,20,[30,40],50]
print(l[0:2]+[l[2][1]])
print(l[0:2]+l[2][:1])

print(l[0:2]+l[2][:2])
print(l[0:2]+l[2][::2])
print(l[0:2]+l[2][1:2])
print(l[0:2]+l[2][0:2])
print(l[0:2]+l[2][0:1])
print(l[2][0])
print(l[2][1])
'''