# def feb():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# f=feb()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# def PowTwoGen():
#     n = 1
#     while n>=1:
#         yield 2 ** n
#         n += 1
# s=PowTwoGen()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# def fibonacci_numbers(nums):
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x+y
#         yield x

# def square(nums):
#     for num in nums:
#         yield num**2
# nums=int(input('enter your range: '))
# print(sum(square(fibonacci_numbers(nums))))

# def all_even():
#     n = 1
#     while True:
#         yield n
#         n += 2
# e=all_even()
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))



