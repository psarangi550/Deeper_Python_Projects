import inspect

def gen_number(n):
    for i in range(n):
        yield i

gen_obj=gen_number(10)
print(gen_obj)

print(next(gen_obj))

print(inspect.getgeneratorstate(gen_number(10)))

print(next(gen_obj))

print(inspect.getgeneratorlocals(gen_obj))

print(inspect.getgeneratorstate(gen_obj))

print(next(gen_obj))

print(inspect.getgeneratorlocals(gen_obj))

print(inspect.getgeneratorstate(gen_obj))

print(next(gen_obj))

print(inspect.getgeneratorlocals(gen_obj))

print(inspect.getgeneratorstate(gen_obj))


###fetching the generator local value as dictionary using the getgeneratorlocal function
