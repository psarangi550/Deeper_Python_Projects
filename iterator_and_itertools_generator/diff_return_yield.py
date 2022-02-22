def return_func(n):
    for i in range(n):
        return i

# print(return_func(20))

#can't be iterate pver as one value being returned at once and the loop terminated 

# return_obj=return_func(20)

# for i in return_obj:
#     print(i)


# def gen_func(n):
#     for i in range(n):
#         yield i

#can be iterate pver as only one value being returned at once
# gen_iter=gen_func(20)

# for i in gen_iter:
#     print(i)