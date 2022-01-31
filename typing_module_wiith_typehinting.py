import typing  # importing the typing module
from typing import List  # importing the List Type hinting with the typing module
from typing import Any
from typing import TypeVar
#here utilising the List of the typing module
def sum_list(l: List[int]) -> int:
    return sum(l)
my_list = [1, 2, 3, 4]
print(sum_list(my_list))

#here also we can use the Any of the typing module

def reflect(a:Any)->Any:
    return a
print(reflect("pratik"))

#creating a type var of add() method descrived below

T= TypeVar("T",int,str,float)
def add(a:T , b:T)->T:
    return a+b

help(add)
print()