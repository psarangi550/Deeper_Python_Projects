# function aliasing
########################################################################
# def wish(name):
#     print("Hello There how you doing",name)
# greeting=wish
# greeting("pratik")
# print(wish)
# print(id(wish))
# print(greeting)
# print(id(greeting))
# print(greeting is wish)
# del wish
# greeting("rika")
# wrapper_nest_func
#######################################################################
# def outer_func():
#     def inner_func():
#         return "Hello"
#     return inner_func
#
# outside_func=outer_func
# outside_inner_func=outside_func()
# print(outside_inner_func())

########################################################################

# def profile(func):
#     print("Outer func profile execution")
#     def inner_func(*args,**kwargs):
#         results=[]
#         if args:
#             for arg in args:
#                 results.append(arg)
#             for result in results:
#                 return "hello "+result
#         else:
#             return "hello"
#     return inner_func
#
# # home=profile
# # view=home()
# # print(view())
#
# #case:-1
# @profile
# def home():
#     print("calling the Hello function")
#
# print(home())
#
# #case:-2
# ##########
# @profile
# def home():
#     print("calling the Hello function")
#
# print(home("rika"))


###################################################################

# def profile(func):
#     print("outer func called")
#     func()
#
#
# def home():
#     print("exec home method")
#
# profile(home)


################################################################

# filter_func
###############

# def input_func(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# x=list(filter(input_func,[10,20,30,40,41]))
# print(x)
#
# x=list(filter(lambda n: input_func(n) ,[10,20,30,40,41]))
# print(x)
#
# x=list(filter(lambda n: True if n % 2 == 0 else False,[10,20,30,40,41]))
# print(x)
# print(list(x))

# map function
#################################

# def input_map(num):
#     return num**2

# print(input_map(2))

# list1=[x for x in range(10)]
# x=map(input_map,list1)
# print(list(x))

###integrating lamda with the map
# list2=[x for x in range(10)]
# x=list(map(lambda n: input_map(n),list2))
# print(x)

# ###onlhy by using the lamda function
# list3=[x for x in range(10)]
# x=list(map(lambda n: n**2 ,list3))
# print(x)

##usage of the reduce module
####################################
from functools import reduce

# def reduce_func(num):
#     result=0
#     for n in num:
#         result+=n
#     return result
#
# list4=[x for x in range(10)]
# x=reduce_func(list4)
# print(x)

##using the lamdas
# list5=[x for x in range(15)]
# # result=0
# x=reduce(lambda num1,num2:num1+num2,list5)
# print(x)

# alternate
############

# def reduce_func(a,b,c):
#     return a+b+c
#
# list6 = [x for x in range(15)]
#
# x: int = reduce(reduce_func,list6)
# print(x)


# def func1(arg1,arg2,arg3=None,arg4=0):
#     print(arg1,arg2,arg3,arg4)
#
# func1(3,4)
# func1(3,4,10,12)
# func1(3,4,arg3=5)
# func1(arg1=1,arg2=3,arg3=5,arg4=5)


# def foo():
#     global a
#     a=20
#     print(a)
# def bar():
#     print(a)
#
# foo()
# bar()
#
# print(globals())


# a=888
# def foo():
#     a=999
#     val=globals()["a"]
#     print(a)
#     print(val)
# foo()


# def fact(num):
#     result=1
#     while num>0:
#         if num == 0 or num == 1:
#             print("Here its executing")
#             result = result*1
#         result=result*num
#         # print(result)
#         num=num-1
#     return result


# print(fact(4))

# a=4
# def fact(num):
#     global a
#     if num==0 or num==1:
#         result=1
#     else:
#         result=num*fact(num-1)
#         a=a-1
#     print(a)
#     return result
import fact as fact


def fact_range(num):
    if num == 0 or num == 1:
        result = 1
    else:
        result = num * fact_range(num-1)
    return result

# print(fact_range(5))

for i in range(10):
    print(fact_range(i))