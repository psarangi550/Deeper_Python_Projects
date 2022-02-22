from memory_profiler import profile

@profile
def count_down(n):
    while n>0: 
        yield n
        n=n-1

if __name__ == '__main__':
    count_down_obj=count_down(10)
    for item in count_down_obj:
        print(item)
