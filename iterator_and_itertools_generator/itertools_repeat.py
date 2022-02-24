import itertools
from math import pow,floor
list_value=[x for x in range(10)]
# print(list_value)
# list1=list(map(lambda x:int(pow(x,2)),list_value))
# print(list1)

# list2=list(map(lambda x:int(pow(x,next(itertools.repeat(2,times=10)))),list_value))
# print(list2)

#alternate approach
list3=list(map(floor,list(map(pow,range(10),itertools.repeat(2)))))
print(list3)