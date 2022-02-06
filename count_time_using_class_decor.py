from time import time,sleep

class evaluate_time_decor(object):
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        time_started=time()
        result=self.func(*args, **kwargs)
        time_ended=time()
        total_dur=time_ended-time_started
        print(total_dur)
        return result

@evaluate_time_decor
def evalueate(num):
    result=[]
    for i in range(num):
        sleep(1)
        result.append(i)
    return result

print(evalueate(10))
