import inspect

def divide(a,b):
    return a/b

def do_something():
    print( divide(a=10,b=0))
    
try:
    do_something()
except ZeroDivisionError as e:
    # print(inspect.trace())
    for frame in inspect.trace():
        print( frame.code_context, end="-")
        print( frame.lineno )
        print()