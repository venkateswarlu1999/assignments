# Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.

# Example: 

# Input: exp = “[()]{}{[()()]()}” 
# Output: Balanced
# Explanation: all the brackets are well-formed

# Input: exp = “[(])” 
# Output: Not Balanced 
# Explanation: 1 and 4 brackets are not balanced because 
# there is a closing ‘]’ before the closing ‘(‘


# brute force

# def vParenthesis(s):
#     while "()" in s or "[]" in s or "{}" in s :
#         s = s.replace("()","").replace("[]",'').replace("{}",'')

#     return len(s)==0

# string = "[()]{}{[()()]()}"
# print(vParenthesis(string))


# def vParenthesis(s):
#     stack = []
#     openingBrackets = '({['
#     closingBrackets = ')}]'

#     for i in s:
#         if i in openingBrackets:
#             stack.append(i)

#         elif i in closingBrackets:
#             if not stack:
#                 return False
#             top = stack.pop()
#             if openingBrackets.index(top) != closingBrackets.index(i):
#                 return False
            
#     return len(s)==0

# string = "[()]{}{[()()]()}"
# print(vParenthesis(string))