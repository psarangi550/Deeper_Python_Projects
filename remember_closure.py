def outer_func(func,message):
    # message="hello"
    def wrapper(*args, **kwargs):
        print(message)
        return func(*args, **kwargs)
    return wrapper


def home(name):
    return "bye"+name

# my_func=outer_func(home)
# # print(my_func)
# print(my_func("pratik"))

my_func=outer_func(home,"holla")
# print(my_func)
print(my_func("pratik"))