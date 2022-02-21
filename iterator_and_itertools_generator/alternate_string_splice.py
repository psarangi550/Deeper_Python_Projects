class StrIter(object):
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return iter(self.value.split())
    def __next__(self):
        list_val=self.value.split()
        # print(list_val)
        index=0
        while index<len(list_val):
            current=index
            index+=1
            return list_val[current]
            
            

# str_iter = StrIter("Hello There")
str_iter = StrIter("My Name is Pratik")
print(str_iter)
# print(str_iter)
# print(next(str_iter))


for str in iter(str_iter):
    print(str)




        
           
       