class RangeIter(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.end:
            raise StopIteration("Are you a Fool")
        else:
            current=self.start
            self.start+=1
            return current

my_rng=RangeIter(10,20)

for i in my_rng:
    print(i)
        