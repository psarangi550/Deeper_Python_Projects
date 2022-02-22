def gen_n_values(n):
    # for i  in range(1,n+1):
    #     yield i
    i=1
    while i<=n:
        yield i
        i+=1

my_gen=gen_n_values(10)

for i in my_gen :
    print(i)