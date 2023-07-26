movies = {
 'actors':{
 'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,
'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},
 'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,
'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
 'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1}, 
'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married',
'sRate':'50%'},
 'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,
'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
 'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2, 
'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50},
 },
 'actress':{
'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1}, 
'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single',
'sRate':'40%'},
 'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 
'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single',
'sRate':'30%'},
 'saipallavi':{'knownAs': 'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 
'remuneration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9,'mStatus':'single',
'sRate':'60%'},
 'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15,
'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},
 'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,
'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'},
 }
}

# 1. Write a program to display all actors names
# for i in movies['actors']: 
#     print(i)

# 2. Write a program to display all actress names
# for i in movies['actress']: 
#     print(i)

# 3. Who is Darling?
# for i in movies['actors']:
#     if movies['actors'][i]['knownAs'] =='Darling':
#         print(i)

# 4. What are the total number of Nandi Awards won by actors?
# l=[]
# sum=0
# for i in movies['actors']:
#     l.append(movies['actors'][i]['awards']['nandi'])
# for i in l:
#     sum+=i
# print(sum)

# 5. What is the name of Prince?
# for i in movies['actors']:
#     if movies['actors'][i]['knownAs']=='Prince':
#         print(i)

# 6. What are the total number of awards own by Ram Charan?
# count=0
# for i in movies['actors']['ramcharan']:
#     if i in 'awards':
#         d=movies['actors']['ramcharan']['awards']
#         for i in d.values():
#             count+=i
# print(' the total number of awards own by Ram Charan: ',count)
    
# 7. Which actor won more number of Nandi Awards?

# 8. What is the success rate of Prince?
# for i in movies['actors']:
#     if movies['actors'][i]['knownAs']=='Prince':
#         print(movies['actors'][i]['sRate'])

# 9. Which actor and actress has more number of Hits?
# 10. Who is Milky Beauty?
# for i in movies['actress']:
#     if movies['actress'][i]['knownAs'] == 'Milky Beauty':
#         print(i)

# 11. What is the nick name of Rashmika?
# for i in movies['actress']:
#     if i == 'rashmika':
#         print(movies['actress'][i]['knownAs'])

# 12. What are actress names who did not win at least one Nandi Award?
# for i in movies['actress']:
#     if movies['actress'][i]['awards']['nandi'] ==0:
#         print(i)

# 13. What are the total number of SIIMA awards won by both actors and actress?
# l=[]
# for i in movies['actors']:
#     l.append(movies['actors'][i]['awards']['siima'])
# for i in movies['actress']:
#     l.append(movies['actress'][i]['awards']['siima'])
# print(sum(l))
    
# 14. What are the actor and actress names who has more success rate?

# 15. What is the age of actor who has more super hit movies?
# l=[]
# for i in movies['actors']:
#     l.append(movies['actors'][i]['hits']['super'])
# for i in movies['actors']:
#      if movies['actors'][i]['hits']['super']==max(l):
#          print(movies['actors'][i]['age'])

# 16. What is the actress name who is married?
# for i in movies['actress']:
#     if movies['actress'][i]['mStatus']=='married':
#         print(i)

# 17. Who is the tallest actress?
# l=[]
# for i in movies['actress']:
#     l.append(movies['actress'][i]['height'])
# for i in movies['actress']:
#     if movies['actress'][i]['height'] == max(l):
#         print(i)

# 18. Who is the Youngest actor and actress?
# l=[]
# l1=[]
# for i in movies['actress']:
#     l.append(movies['actress'][i]['age'])
# for i in movies['actors']:
#     l1.append(movies['actors'][i]['age'])
# for i in movies['actress']:
#     if movies['actress'][i]['age'] == min(l):
#         print(i)
# for i in movies['actors']:
#     if movies['actors'][i]['age'] == min(l1):
#         print(i)

# 19. Who are unmarried actress?
# for i in movies['actress']:
#     if movies['actress'][i]['mStatus'] =='single':
#         print(i)

# 20. Who is smallest actress?
# l=[]
# for i in movies['actress']:
#     l.append(movies['actress'][i]['height'])
# for i in movies['actress']:
#     if movies['actress'][i]['height'] == min(l):
#         print(i)

# 21. Which actress has more Flops?
# l=[]
# for i in movies['actress']:
#     l.append(movies['actress'][i]['hits']['flops'])
# for i in movies['actress']:
#     if movies['actress'][i]['hits']['flops'] == max(l):
#         print(i)

# 22. What is the age of Butter Milky Beauty?
# for i in movies['actress']:
#     if movies['actress'][i]['knownAs']=='Butter Milky Beauty':
#         print(movies['actress'][i]['age'])

# 23. What are the total number of flops of all actress?
# count=0
# for i in movies['actress']:
#     v=movies['actress'][i]['hits']['flops']
#     count=v+count
# print(count)

# 24. What are the ages of Sam and Kaj?
# for i in movies['actress']:
#     if movies['actress'][i]['knownAs']=='Kaj':
#         print(movies['actress'][i]['age'])
#     if movies['actress'][i]['knownAs'] == 'Sam':
#         print(movies['actress'][i]['age'])

# 25. Which actress own highest total number of Awards?

# 26. Who is tallest Actor and Actress?
# hight=[]
# for i in movies['actors']:
#     hight.append(movies['actors'][i]['height'])
# for i in movies['actors']:
#     if movies['actors'][i]['height'] == max(hight):
#         print(i)
# ghight=[]
# for i in movies['actress']:
#     ghight.append(movies['actress'][i]['height'])
# for i in movies['actress']:
#     if movies['actress'][i]['height'] == max(ghight):
#         print(i)

# 27. What are the total number of Industry hits of who has more Success Rate?
# b=[]
# g=[]
# for i in movies['actors']:
#     b.append(movies['actors'][i]['sRate'])
# for i in movies['actors']:
#     if movies['actors'][i]['sRate'] == max(b):
#         print(movies['actors'][i]['hits']['industry'])
# for i in movies['actress']:
#     g.append(movies['actress'][i]['sRate'])
# for i in movies['actress']:
#     if movies['actress'][i]['sRate'] == max(g):
#         print(movies['actress'][i]['hits']['industry'])

# 28. What is the success rate of youngest actress?
# l=[]
# for i in movies['actress']:
#     l.append(movies['actress'][i]['age'])
# for i in movies['actress']:
#     if movies['actress'][i]['age']==min(l):
#         print(movies['actress'][i]['sRate'])

# 29. Who is youngest married actress?
# for i in movies['actress']:
#     if movies['actress'][i]['mStatus']=='married':
#         print(movies['actress'][i]['age'])
# 30. Who is oldest unmarried actor?

# 31. Who are the high successful actor and actress?
# 32. Totally How many unmarried actors and actress are acting in movies?
# 33. Which actress is having more industry hit movies?
# 34. Which actress does not have atleast one industry hit also?
# 35. What are the total number of industry and super hits of tallest actress?
# 36. Which actress is having lengthiest nick name?
# 37. Who are the youngest unmarried actor and actress?
# 38. What are the total number of Industry hits and Super Hits of the actress who got more 
# SIIMA awards?
# 39. What are the ages of Darling and Milky Beauty?
# 40. What are names of actors whose nick name contains star?
# 41. What is the total remuneration of all actors?
# 42. What is the remuneration of an actor who has more flops?
# 43. What is the highest remuneration of an unmarried actress?
# 44. What are the names of actor and actress who has more remuneration?
# 45. What is the remuneration of high successful Actress?
# 46. What is the remuneration of actress who has more industry hits?
# 47. What are the ages of an actors whose remuneration is more then 90 crores?
# 48. What are the total number of industry hits of both Prince and Butter Milky Beauty?
# 49. What is the age of Laughing Queen?
# 50. What are the total number of awards won by an actor who has less successful rate?