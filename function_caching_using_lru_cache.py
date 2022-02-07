import functools
from functools import lru_cache#importing the lru_cache decorator from functools module 
import time #importing the time module
x=int(input("How Many i/p and o/p Calls you want to cache"))
num=int(input("Number of Iteration of Fibonnaci series you want to see"))

@lru_cache(maxsize=x)
def fibo_function(n):
    if n < 2 :#if number is less than 2 then
        return n
    else:
        print(f"calculating the iteration for {n}")
        return fibo_function(n-1)+fibo_function(n-2)

def invoke_fibo_function1(num):
    result=[]
    for i in range(10):
        time.sleep(1)
        result.append(fibo_function(i))
    return result

#checking the time taken by the function cacheing by lru cache


def invoke_fibo_function2(num):
    result=[]
    for i in range(10):
        time.sleep(1)
        result.append(fibo_function(i))
    return result

#without lru_cache
time_started=time.time()
print(invoke_fibo_function1(num))#calling the invoke_fibo_function which will call the fibo_function implicitly
time_ended=time.time()
time_diff=time_ended-time_started
print(time_diff)

#with lru_cache
time_started1=time.time()
print(invoke_fibo_function2(num))#calling the invoke_fibo_function which will call the fibo_function implicitly
time_ended1=time.time()
time_diff1=time_ended1-time_started1
print(time_diff1)  

#lets see how many hit and missises and current size
print(fibo_function.cache_info())