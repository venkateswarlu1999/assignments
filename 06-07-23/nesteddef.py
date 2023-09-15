# def outer():
#     print("outer function starts")
#     def inner():
#         print("inner function executes")
#         print("aman")
#     print("outer function returning inner function")
#     return inner
    
# a=outer()
# a()



# def f():
#     print("this is a ques")
#     def inner(a,b):
#         print("sum is :",a+b)
#     inner(10,20)
#     inner(30,40)
#     inner(20,50)

# f()

# def outer():
#     print("outer function starts")
#     def inner():
#         print("inner function executes")
#         print("aman")
#     print("outer function returning inner function")
#     inner()
    
# outer()

# def outer():
#     print("outer function starts")
#     def inner():
#         print("inner function executes")
#         print("aman")
#         def sinner():
#             print('second inner')
#         print('enter into second inner')
#         return sinner()
#     print("outer function returning inner function")
#     return inner
    
# a=outer()
# a()

# def outer():
#     print("outer function starts")
#     def inner():
#         print("inner function executes")
#         print("aman")
#         def sinner():
#             print('second inner')
#         print('enter into second inner')
#         return sinner()
#     print("outer function returning inner function")
#     souter()
#     return inner
# def souter():
#     print('sencod ouer excuted')
# a=outer()
# a()

# def outer(fun):
#     print("outer function starts")
#     def inner(name):
#         print("inner function executes")
#         if name == 'venky':
#             print('venky is very bad boy')
#         else:
#             fun(name)    
#     return inner
# @outer
# def souter(name):
#     print('sencod ouer excuted')
#     print(name,'is very innocent')
# souter('venky')


# def mainfun(fun):
#     def pro(name):
#         if name == 'venky':
#             print('venky you have good feature')
#         else:
#             fun(name)
#     return pro
# def sub(name):
#     print('your not that much good mr: ',name)
# re=mainfun(sub)
# re('venky')
# re('raju')

# def dec1(fun):
#     def inner():
#         x=fun()
#         return x*x
#     return inner

# def dec2(fun):
#     def inner():
#         x=fun()
#         return 2*x
#     return inner
# @dec2
# @dec1
# def n():
#     return 10
# print(n())   
# decarater=dec2(dec1(n))


# def dec1(fun):
#     def inner(name):
#         print("frist dec execution")
#         fun(name)
#     return inner
# def dec2(fun):
#     def inner(name):
#         print("second dec execution")
#         fun(name)
#     return inner

# @dec2
# @dec1
# def w(name):
#     print("hello",name,"morning")

# w("aman")