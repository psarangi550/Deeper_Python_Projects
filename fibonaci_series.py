# def fibo(n):
#     if n < 2:
#         return n
#     else:
#          return fibo(n-1)+fibo(n-2)

# def invoke_fibo(n):    
#     result=[]
#     for i in range(n):
#         result.append(fibo(i))
#     return result   
# print(fibo(5))
# print(invoke_fibo(5)) 

#[0,1,1,2,3,5]

#without recursion

# def  fibo(n):
#     result=[]
#     a,b=0,1
#     while(n>0):        
#         c=a+b
#         result.append(a)
#         a=b
#         b=c
#         n=n-1
#     return result
            

def  fibo(n):
    result=[]
    a,b=0,1
    while(n>0):        
        c=a+b
        result.append(a)
        a,b=b,c
        n=n-1
    return result       
    
        
print(fibo(7))