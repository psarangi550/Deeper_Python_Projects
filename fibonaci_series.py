def fibo(n):
    if n < 2:
        return n
    else:
         return fibo(n-1)+fibo(n-2)

def invoke_fibo(n):    
    result=[]
    for i in range(n):
        result.append(fibo(i))
    return result   

print(invoke_fibo(5)) 

# print(fibo(5))