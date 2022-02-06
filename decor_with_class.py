from functools import wraps

class decor_class(object):
    def __init__(self,org_func=None):
        self.org_func = org_func
    def __call__(self,*args, **kwargs):
        '''This is a Doc String which belong to decor_class call dunder method'''
        print(self.org_func.__doc__)
        self.org_func(*args, **kwargs)

def decor_fun(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''This is a Doc String which belong to decor_function call using decorator function'''
        # print(func.__doc__)
        func(*args, **kwargs)
    return wrapper

# @decor_class
@decor_fun
def home(name):
    '''This is a Doc String for the original function home'''
    print(home.__doc__)
    print(home.__name__)
    print("Hello "+ name)

home("pratik")