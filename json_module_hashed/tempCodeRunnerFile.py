class DecorHello(object):
    def __init__(self,func):
        self.func = func
    def __call__(self,*args, **kwargs):
        print("Hello There")
        return self.func(*args, **kwargs)

# # @DecorHello
def home(name):
    return "hello "+name

# print(home("pratik"))
decor_hello=DecorHello(home)
print(decor_hello("pratik"))