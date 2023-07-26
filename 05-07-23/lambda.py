 # f = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# re = list(map(lambda x: x, f))
# print(re)

# names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# result = list(filter(lambda name: len(name)>6, names))
# print(result)

# from functools import reduce
# numbers = [4, 6, 9, 23, 5]
# result = reduce(lambda num1, num2: num1+num2, numbers)
# print(result)


s='praveen12345'
l=[]
for i in s:
    if i.isdigit():
        l.append(int(i))
print(l)
sum=0

for i in l:
    sum=sum+i

print(sum)
avarage=sum/100
print(avarage)
