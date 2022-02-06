def decor1(func):
    def wrapper(*args, **kwargs):
        '''this is a doc string related to the wrapper function'''
        print("This function been called using the function {} and args as {}".format(func.__name__,*args,**kwargs))
        return func(*args, **kwargs).upper()
    return wrapper

def hello(name):
    '''This is a doc string in reference to the original function'''
    return "hello"+name

new_fun_var=decor1(hello)
print(new_fun_var.__name__)
print(new_fun_var.__doc__)
print(new_fun_var("pratik"))