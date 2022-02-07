def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


def invoke_factorial(n):
    result=[]
    for i in range(n):
        result.append(fact(i))
    return result

print(invoke_factorial(5))
print(fact(5))
        