# d=dict([{10,'venky'},{20,'raaj'},{30,'rowdy'}])
# d=dict(({10,'venky'},{20,'raaj'},{30,'rowdy'}))
# # d=dict({{10,'venky'},{20,'raaj'},{30,'rowdy'}}) TypeError: unhashable type: 'set'
# d=dict([(10,'venky'),(20,'raaj'),(30,'rowdy')])
# d=dict({(10,'venky'),(20,'raaj'),(30,'rowdy')})
# d=dict(((10,'venky'),(20,'raaj'),(30,'rowdy')))
# d=dict([[10,'venky'],[20,'raaj'],[30,'rowdy']])
# d=dict(([10,'venky'],[20,'raaj'],[30,'rowdy']))
# # d=dict({[10,'venky'],[20,'raaj'],[30,'rowdy']}) TypeError: unhashable type: 'list'
# print(d)

# d = {"don": 100, "sunny": 200, "sai": 1, "shannu": 20}
# sum = 0
# for value in d.values():
#     sum += value
# print(d.values())
# print(sum)

# d = {}
# r = int(input("Enter the number of entries: "))
# for i in range(r):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     d[key] = value
# print(d)
# sum_values=0
# l=[int(i) for i in d.values() if i.isdigit()]
# for i in l:
#     sum_values+=i
# print(sum_values)

# d = {}
# r = int(input("Enter the number of entries: "))
# for i in range(r):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     d[key] = value
# key_length = max(len(key) for key in d.keys())
# print("Table Format:")
# # print(f"{key: <{key_length}} {key}")
# for key in d.keys():
#     print(f"{key: <{key_length}}",end=' ')
# print()
# for value in d.values():
#     print(f"{value: <{key_length}}",end=' ')
# # print(d.keys())


# Write a pro adding the student name and marks from keyboard  and create a dict also display student marks by taking student name as input.
# d = {}
# r = int(input("Enter the number of entries: "))
# for i in range(r):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     d[key] = value
# print(d)
# # print(d['name'])
# # print(d.get('marks'))
# e=input('enter student name to check marks: ')
# if e in d['name']:
#     print(d.get('marks'))

# Number of occurrences of each vowel present in the given string
# st=input('enter any string do you have: ')    
# s=st.lower()
# vowels='aeiou'
# count={}
# for i in vowels:
#     c=s.count(i)
#     count[i]=c
# print(count)


# Number of occurrences of each letter present in the string in Dictionary . aabbcdeaabbceder
# st=input('enter any string do you have: ')
# s=st.lower()  
# d={}
# for i in s:
#     c=s.count(i)
#     d[i]=c
# print(d)

# s='hello word'
# w=s.split()
# r=''.join(reversed(w))
# print(r)

