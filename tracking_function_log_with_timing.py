import logging
import time
def logger_track(func):
    logging.basicConfig(filename=f"{func.__name__}.log", level=logging.WARNING,filemode="a")
    def input_logger(*args, **kwargs):
        logging.warning("function {} called with arguments{}".format(func.__name__,args,kwargs))
        return func(*args, **kwargs)
    return input_logger

def time_tracker(func):
    def wrapper_time(*args, **kwargs):
        time_started=time.time()
        result=func(*args, **kwargs)
        time_ended=time.time()
        total_dur=time_ended-time_started
        print("The Average Time that the function took {} seconds".format(total_dur))
        return result
    return wrapper_time

@time_tracker
@logger_track
def home_func(a,b):
    time.sleep(2)
    return "The addition of %d and %d is %d " % (a,b,(a+b))

print(home_func(15, 2))