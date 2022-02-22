def count_down(n):
    while n >=0:
        yield n
        n-=1

count=count_down(20)

for item in count:
    print (item)