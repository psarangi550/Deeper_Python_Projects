list1=[10,20,30,40]
it=iter(list1)
while True:
    try:
        print(next(it))
    except StopIteration:
        print("All Value accessed")
        break
        
    
    