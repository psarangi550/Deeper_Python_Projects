import inspect
import logging
import time
import functools

logging.basicConfig(level=logging.DEBUG)

def decor_logger(func):
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("executing the decor function {} with arguments {}".format(func.__name__, *args, **kwargs))
        result=func(*args, **kwargs)
        print(func.__doc__)
        logging.info("executing the decor function {} with arguments {}".format(func.__name__, *args, **kwargs))
        return result
    return wrapper

def decor_timer(func):
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_started=time.time()
        result=func(*args, **kwargs)
        time_ended=time.time()
        time_def=time_ended-time_started
        print("the function {} took {} seconds".format(func.__name__, time_def))
        return result
    return wrapper
    

@decor_timer
@decor_logger
def add(a,b):
    
    """
    this function return the result of addition of two objects
    
    """
    return a + b
    
# print(add(10,5))
#removing one layer of decorators
print(inspect.unwrap(add(10,20)))

        