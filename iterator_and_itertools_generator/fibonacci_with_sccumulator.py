import itertools
import operator
list1=[x for x in range(1,10)]

fact_gen=itertools.accumulate(list1,operator.mul)

for item in fact_gen:
    print(item)