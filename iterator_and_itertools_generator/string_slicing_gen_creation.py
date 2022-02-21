def str_gen(value):
    list_val=value.split()
    index=0
    # while index<len(list_val):
    #     yield list_val[index]
    #     index+=1
    while True:
        try:
            yield list_val[index]
            index+=1
        except IndexError as e:
            break
        

my_gen=str_gen("My Name is Pratik")

for i in my_gen:
    print(i) 
            