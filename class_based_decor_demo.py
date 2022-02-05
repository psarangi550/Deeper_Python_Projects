# import kwargs as kwargs


class UpperDecor(object):
    def __init__(self,func):#act as an outer function
        self.func = func
    def __call__(self, *args, **kwargs):#act as an inner function
        return self.func(*args, **kwargs).upper()
    def calling_fun(self,*args,**kwargs):
        return self.__call__(*args,**kwargs)

# @UpperDecor
def home(name):
    return "Hello " + name

# print(home("pratik"))
# upper_decor_fun=home("pratik")
# print(upper_decor_fun)

upper_decor=UpperDecor(home)
print(upper_decor("pratik"))
print(upper_decor.calling_fun("rika"))
