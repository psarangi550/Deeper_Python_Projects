class TopTen(object):
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < 10: 
            val=self.num
            self.num+=1
            return val
        raise StopIteration("Only top 10")

top_ten=TopTen()
print(next(top_ten))

for i in top_ten:
    print(i)