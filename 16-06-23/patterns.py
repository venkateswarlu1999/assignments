'''
for i in range(10, 0, -1):
    for j in range(10, i-1, -1):
        print(j, end=' ')
    print()
'''

# p
# pypy
# pytpytpyt
# pythpythpythpyth
# pythopythopythopythopytho
# pythonpythonpythonpythonpythonpython

# s='python'
# p=[s[:i] for i in range(1,len(s)+1)]
# print(p)
# for i in p:
#     print(i*(len(i)))

# p='python'
# q=""
# r=0
# for i in p:
# 	q+=i
# 	r+=1
# 	print(q*r)

# word= "Python"
# for i in range(1,len(word)+1):
#     new=""
#     for j in range(i):
#         new=new+(word[j])

#     print(new*i)


# string = "python"
# pattern = ""

# for i in range(1, len(string) + 1):
#     pattern = ""
#     for j in range(i):
#         pattern += string[j]
#     pattern = pattern * i
#     print(pattern)


# python
# pytho
# pyth
# pyt
# py
# p
# python
# pytho
# pyth
# pyt
# py
# p

# s='python'
# p =[s[:i] for i in range(1,len(s)+1)]
# # print(p)
# print(*(p+p[::-1]),sep='\n')
# p=[s[:i] for i in range(len(s),0,-1)]
# print(*(p+p),sep='\n')



#  p
#  py
#  pyt
#  pyth
#  pytho
#  python
#  pytho
#  pyth
#  pyt
#  py
#  p

#S = input("Enter the word: ") #For user input.
# S = ' python'
# length = len(S)

# for i in range(1, length + 1):
#     pattern = ""
#     for j in range(i):
#         pattern += S[j]
#     print(pattern)

# for i in range(length - 1, 0, -1):
#     pattern = ""
#     for j in range(i):
#         pattern += S[j]
#     print(pattern) 

#or

# for i in range(1, length + 1):
#     pattern = S[:i].capitalize()
#     print(pattern)

# for i in range(length - 1, 0, -1):
#     pattern = S[:i].capitalize()
#     print(pattern)
    
# word= "Python"
# for i in range(1,len(word)+1):
#     for j in range(i):
#         print(word[j],end="")
#     print()
# for i in range(1,len(word)+1):
#     for j in range(len(word)-i):
#         print(word[j],end="")
#     print() 




# Pattern #1:

# 1  

# 2 2  

# 3 3 3  

# 4 4 4 4  

# 5 5 5 5 5

# r=int(input('enter range of your pattern: '))
# for i in range(1,r):
#     for j in range(1,i+1):
#         print(i, end=' ')
#     print()

# num=0
# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     for j in range(i+1):
#         num+=(i+1)-num
#         print(num, end=' ')
#     print()

# Pattern #2:

# 1 

# 1 2 

# 1 2 3 

# 1 2 3 4 

# 1 2 3 4 5

# r=int(input('enter range of your pattern: '))
# for i in range(0,r):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# Pattern #3: 

# 1 

# 2 1 

# 3 2 1 

# 4 3 2 1 

# 5 4 3 2 1

# r=int(input('enter range of your pattern: '))
# for i in range(0,r):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print()

# Pattern #4: 

# 1 

# 2 3 4 

# 5 6 7 8 9

# num=1
# r=int(input('enter range of your pattern: '))
# for i in range(0,r,2):
#     for j in range(i+1):
#         print(num, end=' ')
#         num+=1
#     print()

# Pattern #5: 

# 1

# 3 2

# 6 5 4

# 10 9 8 7



# Pattern #6:

# 1 

# 1 2 1 

# 1 2 3 2 1 

# 1 2 3 4 3 2 1 

# 1 2 3 4 5 4 3 2 1

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     for j in range(i-1,0,-1):
#         print(j,end=' ')
#     print()

# Pattern #7: 

# 10 

# 10 8 

# 10 8 6 

# 10 8 6 4 

# 10 8 6 4 2

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(i):
#         print(2*(r-j), end=' ')
#     print()

# Pattern #8:

# 0  

# 0 1  

# 0 2 4  

# 0 3 6 9  

# 0 4 8 12 16  

# 0 5 10 15 20 25  

# 0 6 12 18 24 30 36

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(i+1):
#         print(i*j, end=' ')
#     print()

# Pattern #9: 

# 1 

# 3 3 

# 5 5 5 

# 7 7 7 7 

# 9 9 9 9 9

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(i):
#         print((2*i-1), end=' ')
#     print()

# Pattern #10: 

# * 

# * * 

# * * * 

# * * * * 

# * * * * *

# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     for j in range(i+1):
#         print('*', end=' ')
#     print()

# Pattern #11:

# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# num=1
# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     for j in range(i+1):
#         print(num, end=' ')
#         num-=1
#     print()
#     num+=(i+1)+1

# Pattern #12:

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num=1
# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     for j in range(i+1):
#         print(num, end=' ')
#         num+=1
#     print()
############################################################################


# Pattern #13: 

# 1 1 1 1 1 

# 2 2 2 2 

# 3 3 3 

# 4 4 

# 5

# for i in range(1,6):
#     for j in range(6-i):
#         print(i, end=' ')
#     print()




# Pattern #14: 

# 5 5 5 5 5 

# 4 4 4 4 

# 3 3 3 

# 2 2 

# 1

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i, end=' ')
#     print()


# Pattern #15: 

# 5 5 5 5 5 

# 5 5 5 5 

# 5 5 5 

# 5 5 

# 5

# for i in range(1,6):
#     for j in range(6-i):
#         print(5, end=' ')
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print(5, end=' ')
#     print()




# Pattern #16: 

# 0 1 2 3 4 5 

# 0 1 2 3 4 

# 0 1 2 3 

# 0 1 2 

# 0 1

# for i in range(5):
#     for j in range(6-i):
#         print(j, end=' ')
#     print()






# Pattern #17:

# 5 4 3 2 1 1 2 3 4 5 

# 5 4 3 2 2 3 4 5 

# 5 4 3 3 4 5 

# 5 4 4 5 

# 5 5

# r=int(input('enter range of your pattern: '))

# for i in range(1,r+1):
#     for j in range(r,i-1,-1):
#         print(j,end=' ')
#     for j in range(i,r+1):
#         print(j,end=' ')
#     print()


###################################################

# Pattern #18:

#            1 

#          1 2 

#        1 2 3 

#      1 2 3 4 

#    1 2 3 4 5

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(r-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


##################################################

# Pattern #19: 

#       *   
#      * *   
#     * * *   
#    * * * *   
#   * * * * *   
#  * * * * * *   
# * * * * * * *

# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     print(' '*(r-i)+' * '*(i))
########################################################


# Pattern #20: 

# * * * * * * 
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 
# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     print(' '*i+' * '*(r-i))

# Pattern #21:

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     print(' '*(r-i)+'* '*(i))
# for i in range(r):
#     print(' '*i+'* '*(r-i))

#########################################################

# Pattern #22:

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     for j in range(r):
#         print('*', end=' ')
#     print()

# Pattern #23:

# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     for j in range(1,r+1):
#         print(j, end=' ')
#     print()

# Pattern #24:

# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         print(i, end=' ')
#     print()

# Pattern #25:

# 5 5 5 5 5 
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         print(r+1-i, end=' ')
#     print()

# Pattern #26:

# 5 4 3 2 1 
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1

# r=int(input('enter range of your pattern: '))
# for i in range(1,r+1):
#     for j in range(1,r+1):
#         print((r+1)-j,end=' ')
#     print()


#       *             *                
#      * *           * *   
#     * * *         * * *   
#    * * * *       * * * *   
#   * * * * *     * * * * *   
#  * * * * * *   * * * * * *   
# * * * * * * * * * * * * * *

# r=int(input('enter range of your pattern: '))
# for i in range(r):
#     print(' '*(r-i)+'* '*(i),end=' ')
#     print(' '*(r-i)+'* '*(i))