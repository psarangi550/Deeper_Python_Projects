class ListMirror(object):
    def __init__(self,value):
        self.value = value
    def __iter__(self):#here we are creating the iterator class as iterable __iter__ method will create iterator object
        return iter(self.value)

list_mirror=ListMirror([10,20,30,40])

for i in list_mirror:
    print(i)