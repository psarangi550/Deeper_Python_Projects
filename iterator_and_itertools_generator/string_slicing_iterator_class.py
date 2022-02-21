class StrIter(object):
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self.value
    def __next__(self):
        list_val=self.value.split()
        iter_val=iter(list_val)
        return iter_val

# str_iter = StrIter("Hello There")
str_iter = StrIter("My Name is Pratik")
# print(str_iter)
# print(next(str_iter))

for str in next(str_iter):
    print(str)

# for str in next(str_iter):
#     print(str_iter)




        
           
       