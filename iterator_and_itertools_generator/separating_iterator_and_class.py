class ListInput(object):
    def __init__(self, list_value):
        self.list_value = list_value
    def __iter__(self):
        return ListIter(self.list_value)
    def display(self):
        print("Iterating using the Another ListIter class ")

class ListIter(object):
    def __init__(self,list_value):
        self.list_value = list_value
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.list_value):
            current=self.index
            self.index = self.index + 1
            return self.list_value[current]
        raise StopIteration()

#================================================================

list_input_obj=ListInput([10,20,30,40,50])
list_iter_obj=ListIter(list_input_obj)
# print(list_input_obj)
# print(list_iter_obj)

for item in list_input_obj:
    print(item)
        