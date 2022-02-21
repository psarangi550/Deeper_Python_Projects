class StrIter(object):
    def __init__(self, value):
        self.value = value
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        list_val=self.value.split(' ')
        if self.index>len(list_val):
            raise StopIteration("Are you foolish ?")
        else:
            current=self.index
            self.index+=1
            return list_val[current]

str_iter=StrIter("Hello There Rika")


for i in str_iter:
    print(i)
    
        
        
        