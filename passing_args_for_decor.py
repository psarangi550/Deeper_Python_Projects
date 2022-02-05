def outer_decor(name):
    print("The Decorator args provided as %s " % name)
    def inner_decor(func):
        def wrapper(*args, **kwargs):
            original_input = func(*args, **kwargs)
            modified_input = original_input.upper()
            return modified_input
        return wrapper
    return inner_decor


@outer_decor("pratik")
def home(name):
    return "Hello "+ name

print(home("Rika"))
