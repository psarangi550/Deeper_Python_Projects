def generate_gen():
    yield "A"
    yield "B"
    yield "C"

generator_gen=generate_gen()

# for i in generator_gen:
#     print(i)

while True:
    try:
        print(next(generator_gen))
    except StopIteration as e:
        print((e))
        break