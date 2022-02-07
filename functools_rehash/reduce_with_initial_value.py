from functools import reduce
list1=[x for x in range(101)]
sum_list=reduce(lambda x,y:x+y,list1, 10)
print(sum_list)

