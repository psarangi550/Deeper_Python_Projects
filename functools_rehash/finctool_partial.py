
from functools import partial

def add(a,b):
    print("a value is ",a)
    print("b value is ",b)
    return a + b

#case:-1
new_add=partial(add,1)
print(new_add(10))

#case:-2
new_add=partial(add,b=1)
print(new_add(10))

#case:-3 #error as we assgning 2 value to the a
# new_add=partial(add,a=1)
# print(new_add(10))

#solution
new_add=partial(add,a=1)
print(new_add(b=10))