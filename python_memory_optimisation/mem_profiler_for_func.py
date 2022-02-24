from memory_profiler import profile,memory_usage
import time

# mem_usage=memory_usage(-1,timeout=1,interval=0.2)
# list_all=[x**2 for x in range(10)]
# print(mem_usage)

# mem_usage=memory_usage(-1,interval=1)
# list1=[]
# for i in range(10):
#     list1.append(i*i)
#     time.sleep(1)
# print(mem_usage)

list1=[]
mem_usage=memory_usage()
def list_count(num):
    for i in range(num):
        # time.sleep(1)
        list1.append(i*i)
        


list_count(10)
mem_usage1=memory_usage((list_count,(10,)),timeout=10,interval=10)
print(mem_usage)
print(mem_usage1)