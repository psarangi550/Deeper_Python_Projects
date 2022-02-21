class StrIter(object):
    def __init__(self, value):
        self.value = value
        self.index = 0
        self.current=0
    def __iter__(self):
        print(self)
        return self
    def __next__(self):
        list_val=list(self.value)
        # return iter(list_val)
        if self.index < len(self.value):
                self.current=self.index
                self.index+=1
                return self.value[self.current]
        else:
            raise StopIteration()
                           
str_iter = StrIter("Hello")

# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))


for i in str_iter:
    print(i)
