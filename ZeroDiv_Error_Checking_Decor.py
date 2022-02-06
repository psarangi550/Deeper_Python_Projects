# class Zero_Dev_Error_Checking_Decorator(object):
#     def __init__(self,func):
#         self.func = func
#     def __call__(self, *args,**kwargs):
#         print(kwargs)
#         if "b" in kwargs and kwargs["b"]==0:
#             return "cant divide it by zero"
#         else:
#             return self.func(*args,**kwargs)
#
# @Zero_Dev_Error_Checking_Decorator
# def division_fun(a,b):
#     return a/b
#
# print(division_fun(a=10,b=0))


####reversiong the process

# def check_zero_dev_error(func):
#     def wrapper(div_obj):
#         if div_obj.b==0:
#             return "Can't divide it by zero"
#         else:
#             return func(div_obj)
#     return wrapper
#
# class division_number(object):
#     def __init__(self,a=None,b=None):
#         self.a=a
#         self.b=b
#     @check_zero_dev_error
#     def division_function(self):
#         return self.a/self.b
#
# d=division_number(a=10,b=2)
# print(d.division_function())


def check_zero_dev_error(func):
    def wrapper(*args,**kwargs):
        for arg in args:
            if arg.b==0:
                return "can't divide it by zero"
            else:
                return func(arg)
    return wrapper

class division_number(object):
    def __init__(self,a=None,b=None):
        self.a=a
        self.b=b
    @check_zero_dev_error
    def division_function(self):
        return self.a/self.b

d=division_number(a=10,b=0)
print(d.division_function())
