from functools import singledispatch

# def add_one(obj):
#     if isinstance(obj,list):
#         return obj+[1]
#     if isinstance(obj,set):
#         return obj.union({1})
#     if isinstance(obj,str):
#         return obj+str(1)
#     if isinstance(obj,int):
#         raise ValueError("Int value not allowed")

# print(add_one([1,2,3,5]))
# print(add_one({2,3,5}))
# print(add_one("1234"))
# print(add_one(1234))


#now implemeting using the singledispatch decorator

@singledispatch
def add_many(obj):
    # pass
    if isinstance(obj,int):
        raise ValueError("Int value not allowed")

#creating the generic function which is a cumulation of multiple functions of same execution style for different data type
#1st approach using type hinting is:-
################################
# @add_many.register
# def _(obj:list):
#     return obj+[1]

# @add_many.register
# def _(obj:str):
#     return obj+str(1)

# @add_many.register
# def _(obj:set):
#     return obj.union({1})

#2nd approach using normal class is:-
################################
@add_many.register(list)
def _(obj):
    return obj+[1]

@add_many.register(str)
def _(obj:str):
    return obj+str(1)

@add_many.register(set)
def _(obj:set):
    return obj.union({1})

print(add_many([1,2,3,4,5]))
print(add_many({2,3,5}))
print(add_many("1234"))
print(add_many(1234))

        