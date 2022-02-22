import time
class Student(object):
    def __init__(self,first,last,roll):
        self.first=first; self.last=last;self.roll=roll
    def __str__(self):
        return self.first
    def __repr__(self):
        return f"{self.first}-{self.last}-{self.roll}"
stu_list=[]

#time taken by the list of students
# 2.202352285385132

# while True:
#     first=input("select first Name")
#     last=input("select last Name")
#     roll=int(input("select roll number"))
#     start_time=time.time()
#     stu=Student(first=first, last=last, roll=roll)
#     stu_list.append(stu)
#     option=input("Do you wish to add a new student [y/n]:")
#     if option.lower()=="n":
#         end_time=time.time()
#         time_diff=end_time-start_time
#         print(time_diff)
#         break

#time taken by the generator of students
# 1.608280897140503 #time taken by the generator 
def get_stu_gen():
    while True:
        first=input("select first Name")
        last=input("select last Name")
        roll=int(input("select roll number"))
        start_time=time.time()
        stu=Student(first=first, last=last, roll=roll)
        yield stu
        option=input("Do you wish to add a new student [y/n]:")
        if option.lower()=="n":
            end_time=time.time()
            time_diff=end_time-start_time
            print(time_diff)
            break

gen_obj=get_stu_gen()

for item in gen_obj:
    print(item)