import functools
def decor1(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        '''This is the doc string for the wrapper function '''
        return func(*args,**kwargs)#calling the original  input function
    return wrapper

@decor1#calling the decorator
def home(name):
    '''This is the doc string for the home original function'''
    print(home.__name__)#printing the name of the function class
    print(home.__class__.__name__)#the class name of the parent function will be executed in this case
    print(home.__doc__)#printing the name of the doc string
    return "hello "+name

print(home("pratik"))
