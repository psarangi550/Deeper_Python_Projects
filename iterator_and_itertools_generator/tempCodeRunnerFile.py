class ListMirror(object):
    def __init__(self,value):
        self.value = value
    def __iter__(self):
        return iter(self.value)

list_mirror=ListMirror([10,20,30,40])

for i in list_mirror:
    print(i)