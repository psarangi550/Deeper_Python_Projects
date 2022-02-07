x=input("Enter a Number")

def arms(x):
    list1=list(x)
    result=0
    for i in list1:
        result=result+int(i)**len(list1)
    if result==int(x):
        print("number is an armstrong number")
    else:
        print("its not an armstrong number")

arms(x)
# arms(153)