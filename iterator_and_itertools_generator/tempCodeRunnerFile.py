class ListInput(object):
    def __init__(self, list_value):
        self.list_value = list_value

class ListIter(object):
    def __init__(self,list_input):
        self.list_input = list_input
        self.index=0
    def __iter__(self):
        return self.list_input
    def __next__(self):
        list_val=list(self.list_input)
        if self.index > len(list_val):
            raise StopIteration("check this out")
        if self.index < len(list_val):
            current=self.index
            self.index = self.index + 1
            return list(list_input[current])

#================================================================

list_input_obj=ListInput([10,20,30])
list_iter_obj=ListIter(list_input_obj)
# print(list_input_obj)
# print(list_iter_obj)

for item in list_iter_obj:
    print(item)
        