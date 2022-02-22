def fibo_gen(n):
    a,b,c,i=0,1,1,0
    while i < n:
        yield a
        a=b
        b=c
        c=a+b
        i=i+1

fibo_gen_object=fibo_gen(10)

# for i  in fibo_gen_object:
#     print(i,end=' ')

#using the while loop
###here we are using the next() for this 
count=1
while count<=5:
    print(next(fibo_gen_object))
    count=count+1