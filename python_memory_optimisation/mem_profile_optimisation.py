import memory_profiler as mem_profiler
# from mem_profiler import profile

# with open("mem.log","w")as f:
    # @mem_profiler.profile(precision=2,stream=f)
def count_down(n):
    while n>0: 
        yield n
        n=n-1
            
fp=open("mem.log","w")
@mem_profiler.profile(precision=2,stream=fp)
def count_up():
    x=[x*x for x in range(1000)]

if __name__ == '__main__':
    # count_down_obj=count_down(10)
    # for item in count_down_obj:
    #     print(item)
    count_up()
