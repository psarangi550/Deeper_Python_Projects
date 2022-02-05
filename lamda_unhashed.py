# lambda example:-
################
# s=lambda n:n*n
# print(s(2))
#
# def foo(x):
#     for i in range(10):
#         print(x)
#
#
#
# def foo():
#     result=0
#     for i in range(10):
#         result=result+i
#     return result


# print(foo())


# d=reduce(lambda num1,num2: num1+num2 ,[x for x in range (10)])
# print(d)
# s= lambda n :[i+1 for i in range(10)]
# print(s(4))
# import i as i

# s=lambda :[i+i for i in [2,4,6,8]]
# print(s())
# print(s)
# print(type(s))
#
# #with map function
# s=map(lambda a: a+a, [2,4,6,8])
# print(list(s))

#
# s=lambda:[i.capitalize() for i in ["my", "python"]]
# print(s())
#
# s=map(lambda a:a.upper(),["My","Python"])
# print(list(s))

# def input_func(l):
#     result=[]
#     for l1 in l:
#         if l1%2==0:
#             result.append(l1)
#     return result
#
# s=lambda a: input_func (a)
# print(s([2,4,5,6,7,8]))
# s=filter(lambda i: True if i%2==0 else False,[i for i in range(10)])
# print(list(s))

# list1=[12,3,9,1,2,4,5]
# tup1=[("9B",36),("9A",35),("9C",37)]
# # s=lambda a: list(sorted(a))
# # print(s(list1))
# s=lambda a: a.sort()
# s(list1)
# print(list1)

# l1=sorted(tup1,key=lambda a:a[0])
# print(list(l1))

# import math
#
# list2 = [36, 39, 32, 30, 33, 35, 37, 34]
# # avg=sum(list2)/len(list2)
# # print(avg)
# s1 = sorted(list(filter(lambda a: True if a >= math.floor(sum(list2) / len(list2)) else False, list2)))
# print(list(s1))


# countries=["india","UAE","France","USA","Germany","Austria"]
# s3=sorted(list(filter(lambda a: True if len(a)>3 else False, countries)))
# print(list(s3))

# from functools import reduce
# list1=[x for x in range(15)]
# x=reduce(lambda a,b: max(a,b),list1)
# print(x)

#lamda with nested list
import countries as countries

# score=[[1,37,80],[2,32,78],[3,38,98],[4,33,85]]
# s4=map(lambda score:score[2]+2 if score[1]>35 else score[2]-2,score)
# # print(s4)
# # for i in s4:
# #     print(i)
# print(list(s4))
# # print(s4(score))
#
# #lamda with dict
# details=[{"country":"india","sales":150.5},
#          {"country":"America","sales":350.5},
#          {"country":"china","sales":250.5}
#         ]
# s5=map(lambda x: f'{x["country"]}-->{x["sales"]}',details)
# print(list(s5))
# s6=filter(lambda a:a if a.get("sales")>151 else False ,details)
# print(list(s6))

####lamda with multiple list
# list1=[10,20,30,40]
# list2=[50,60,70,80]
# s7=map(lambda a,b : a+b, list1,list2)
# print(list(s7))

#ternary operator with lambda
########################################

# s=lambda a,b,c : a if a>b
# and a>c else b if b>c else c
# print(s(2,15,6))

################################


# list1=[x for x in range(10)]
# f=filter(lambda x: x%2==0,list1)
# print(list(f))

# list1=[x for x in range(10)]
# l1=list(filter(lambda x: x%2!=0 and x%3==0,list1))
# print(l1)

# import re
# list1=["rika","abi","gundu","rikun"]
# l2=list(filter(lambda x: re.match("r",x),list1))
# print(l2)


# import keyword
# print(keyword.kwlist)

# import math
# list1=[x for x in range(10)]
# l3=list(map(lambda a: int(math.pow(a,2)),list1))
# print(l3)
# import list1 as list1

# list1=[[1,2,3,4],[5,6,7,8]]
# from functools import reduce
# l3=reduce(lambda a,b : [sum(a)for i in a]+[sum(a)for i in b], list1)
# print(l3)

################################

import importlib
print(dir(importlib))