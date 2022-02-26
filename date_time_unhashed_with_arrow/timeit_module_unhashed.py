import timeit
import time
# print(timeit.timeit(stmt='x=0',setup='',timer=time.perf_counter,number=100000,globals=None))
#checking betweek while and forloop which one is faster 
# #while loop using as 
# print(timeit.timeit(stmt='while x<100000:x+=1',setup='x=0',timer=time.perf_counter,number=1,globals=None))

#o/p:-
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$ python3 timeit_module_unhashed.py
# 0.0037573000008706003
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$ pypy3 timeit_module_unhashed.py
# 0.0006405000003724126
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$

#for loop we can use that as 
# print(timeit.timeit(stmt='for x in range(100000):pass',setup='',timer=time.perf_counter,number=1,globals=None))

# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$ python3 timeit_module_unhashed.py 
# 0.0008940999996411847
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$ pypy3 timeit_module_unhashed.py 
# 0.0005569000004470581
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$

#using the semicolon to make the difference between the statement indent as below 
#here we are using the process_time instead of perf_counter which will calculate the process time 
#here the wait time will be considered as the process time
#but in case of perf_counter it will not be calculated
#in windows time.perf_counter==time.process_time

# print(timeit.timeit(stmt='x=0;y=0',setup='',timer=time.process_time,number=100000000,globals=None))
# print(timeit.timeit(stmt='while x<1000000000:x+=1;y+=1',setup='x=0;y=0',timer=time.process_time,number=1,globals=None))  


#o/p:-
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$ python3 timeit_module_unhashed.py 
# 2.203125
# 53.3125
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$ pypy3 timeit_module_unhashed.py 
# 0.03125
# 0.6875

#now we can use multiple timeit function as well
#but instead we can use the repeat() function for the same 
# print(timeit.timeit(stmt='x=0;y=0',setup='',timer=time.process_time,number=100000000,globals=None))
# print(timeit.timeit(stmt='x=0;y=0',setup='',timer=time.process_time,number=100000000,globals=None))
# print(timeit.timeit(stmt='x=0;y=0',setup='',timer=time.process_time,number=100000000,globals=None))
# print(timeit.timeit(stmt='x=0;y=0',setup='',timer=time.process_time,number=100000000,globals=None))

#same can be written as this this will provide a list as an output
# print(timeit.repeat(stmt="x=0;y=0",setup='',timer=time.perf_counter,number=1, repeat=4,globals=None))

#o/p:-
#-----------------
# (base) pratik@TE1GXB2J3:/mnt/c/Users/611903295/Downloads/All New Python Concept/date_time_unhashed_with_arrow$ pypy3 timeit_module_unhashed.py 
# 0.046875
# 0.046875
# 0.03125
# 0.04687500000000003
# [2.9000002541579306e-06, 5.000001692678779e-07, 3.9999940781854093e-07, 5.000001692678779e-07]

#definging the function and counting it value after 4 repeat for 4 times execution

# def timeit_func():
#     for x in range(1000000):
#         pass

#global always been executed inside the namespace of timeit module by default 
#hence we need to set the setup so that it will be able to fetch the function in the timeit namespace in order to execute
# print(timeit.repeat(stmt='timeit_func()',setup='from __main__ import timeit_func',timer=time.perf_counter,number=4,repeat=4))
#alternatively we can also use the globals() which will provvide the dictionary of global variable available in the model hence the function will be included
#here don't have to set up anything as we are accessing the global namespace of time it module as global() which contains the dict which have all the global variable as per the module
# print(timeit.repeat(stmt='timeit_func()',setup='',timer=time.perf_counter,number=4,repeat=4,globals=globals()))