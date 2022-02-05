# def outer_profile(func):
#     def inner_profile(*args):
#         for arg in args:
#             func(arg)
#             print("Thanks in advance")
#     return inner_profile
#
#
# def profile(func):
#     def wrapper(*args):
#         for arg in args:
#             func(arg)
#             print("How you doing")
#     return wrapper
#
# @outer_profile
# @profile
# def home(*args):
#     for arg in args:
#         print("Hello", arg)


# new_func_1=outer_profile(profile(home))
# new_func=profile(home)
# new_func_1("Pratik")
# home("Pratik")

#
# def decor(func):
#     def wrapper(*args):
#
#         for arg in args:
#             if arg=="rika":
#                 print("Hello There")
#                 func(arg)
#             else:
#                 func(arg)
#
#     return wrapper
#
# @decor
# def wish(name):
#     print("Hey", name)
#
# wish("pratik")
# wish("rika")


# def smart_div(func):
#     def wrapper(a,b):
#         if b !=0:
#             return func(a,b)
#         else:
#             return "Are you high"
#     return wrapper
#
# @smart_div
# def division_func(a,b):
#     return a/b
#
# print(division_func(10,0))


###switch on and switch off the decoratator
################################################
# def decor(func):
#     def wrapper(*args):
#
#         for arg in args:
#             if arg=="rika":
#                 print("Hello There")
#                 func(arg)
#             else:
#                 func(arg)
#
#     return wrapper
#
#
# def wish(name):
#     print("Hey", name)
#
# new_func=decor(wish)
# new_func("rika")
# new_func("pratik")
#
# # wish("pratik")
# # wish("rika")



####chaining of decorator
########################################################################

# def decor1(func):
#     def inner_func1(*args):
#         print("inner function 1")
#         func(*args)
#     return inner_func1
# def decor2(func):
#     def inner_func2(*args):
#         print("inner function 2")
#         func(*args)
#     return inner_func2
# def decor3(func):
#     def inner_func3(*args):
#         print("inner function 3")
#         home(*args)#here we are calling the method which call the decorators hence it will be in a loop and recusion error will happen
#
#     return inner_func3
#
# @decor3
# @decor2
# @decor1
# def home(name):
#     print("hello",name)
#
# home("pratik")




#####here checking all the py interpreter
################################################################

# '''
# here are few doc string
#
# '''
#
#
#
# # print(__file__,end="-")
# # print(__doc__)
# #
# import os
# # print(os.path.abspath(os.path.dirname(__file__)))
# # print(os.path.abspath(__file__)=="C:\\Users\\611903295\\Downloads\\All New Python Concept\\decorator_unhashed.py")

# print(__package__)

# x=10

def func():
    return 10
print(func.__class__.__name__)

















