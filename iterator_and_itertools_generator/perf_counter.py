import time
import memory_profiler
import random

# stu_name=["pratik","rika","abi","gundu"]
# subject=["python","django","flask","sql","plsql",]
# result=[]#empty list
# memory_before="Memory Before {}".format(memory_profiler.memory_usage())
# print(memory_before)
# @memory_profiler.profile(precision=2)
# def list_func(num):
#     for i in range(num):
#         student ={
#             "id":i,
#             "name":random.choice(stu_name),
#             "subject":random.choice(subject)
#         }
#         result.append(student)
#         return result

stu_name=["pratik","rika","abi","gundu"]
subject=["python","django","flask","sql","plsql",]
# @memory_profiler.profile(precision=2)  
memory_before="Memory Before {}".format(memory_profiler.memory_usage())
print(memory_before)
def gen_func(num):
    for i in range(num):
        student ={
            "id":i,
            "name":random.choice(stu_name),
            "subject":random.choice(subject)
        }
        yield student

# start_time = time.perf_counter()
# list_func(10000)#calling the function
# end_time = time.perf_counter()
# time_difference = end_time - start_time
# print(time_difference)
# memory_after="Memory After {}".format(memory_profiler.memory_usage())
# print(memory_after)

start_time = time.perf_counter()
gen_func(10000)#calling the function
end_time = time.perf_counter()
time_difference = end_time - start_time
print(time_difference)
memory_after="Memory After {}".format(memory_profiler.memory_usage())
print(memory_after)

