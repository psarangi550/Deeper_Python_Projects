import inspect
import functools

@functools.lru_cache(maxsize=128)
def test_add(a,b):
    '''executing the add function'''
    return a + b

print(test_add) # this will point to the lru_cache function

print(inspect.unwrap(test_add)) #this will point to the original function


