import logging
from functools import wraps
logging.basicConfig(filename="logging.log",level=logging.INFO,filemode="a")

def logger_function(func):
    def inner_logger(*args, **kwargs):
        logging.warning("The Function executing is {} and the args is {}".format(func.__name__,*args,**kwargs))
        return func(*args, **kwargs)
    return inner_logger

def add(a,b):
    return a + b

def remove(a,b):
    return a-b

new_function1=logger_function(add)
print(new_function1(10,20))


new_function2=logger_function(remove)
print(new_function2(100,20))