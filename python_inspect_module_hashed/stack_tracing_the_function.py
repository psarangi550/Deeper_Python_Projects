import inspect

def add(a,b):
    stack_trace=inspect.stack()
    for frame in stack_trace:
        print(frame.code_context)
        # print(frame.lineno)
    print(a + b)

def get_method():
    add(10,20)
    

get_method()