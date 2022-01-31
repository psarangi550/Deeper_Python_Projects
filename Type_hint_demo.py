# here i am implementing the type hinting in python which is the new format of writing code
from datetime import datetime
# def avg_meal_price(meal_value: float, person: int, tip: float = 0.2) -> float:
#     result_price: float = (meal_value + tip) / person
#     return result_price


# print(avg_meal_price(145.55, 4))

class DaysOfwork(object):
    def __init__(self,days:int)->None:
        self.days=days
    def __str__(self)->str:
        return f"{self.days}"

class Employee(object):
    name:str = 'abi'
    raise_amount:float = 1.05

    def __init__(self, first:str, last:str,pay:int=5000)->None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email:str = f"{self.first}.{self.last}@email.com"
        return None

    def invoke_format_string_input(self, input_str:str)->"Employee":
        return Employee.format_string_input(input_str)
    @classmethod
    def format_string_input(cls, input_str:str)->"Employee":
        print(cls)
        print(input_str.split("-"))
        first = input_str.split('-')[0]
        last = input_str.split('-')[1]
        return cls(first=first, last=last)

    @staticmethod
    def fetch_work_day(date_input):
        date_day=date_input.strftime("%A")
        print(date_day)
        work_day=["monday","tuesday","wednesday","thrusday","friday"]
        if date_day.lower() in work_day:
            print ("working day")
        else:
            print("weekend")

    # def __add__(self,other):
    #     if not isinstance(other,Employee):
    #         return "other should be an instance of Employee"
    #     return self.pay+other.pay

    def __add__(self, *args)->"Employee":
        result=self.pay
        for arg in args:
            if not isinstance(arg, Employee):
                return NotImplemented
            result+=arg.pay
        return Employee(first="",last="",pay=result)

    def __mul__(self,other):
        if not isinstance(other,DaysOfwork):
            return NotImplemented
        return self.pay * other.days

    def __str__(self)->str:
        return f"Emp First Name{self.first},Emp Last Name {self.last}"

    def __repr__(self)->str:
        return f" Employee Salary is {self.pay}"



# e1 = Employee.format_string_input("pratik-kumar")
# print(e1)
# print(e1.first)
# print()

# emp1=Employee(first="pratik",last="sarangi")
# emp2=emp1.invoke_format_string_input("rika-sarangi")
# print(emp2)
# print(emp2.first)
# print(emp2.last)

# Employee.fetch_work_day(datetime(2022,10,9))

# emp1=Employee("pratik","sarangi",11000)
# # print(emp1)
# emp2=Employee("rika","sarangi",8000)
# # print(emp2)
# emp3=Employee("abi","sarangi",10000)
# print(emp3)
# print(repr(emp1+emp2+emp3))
# print(str(emp1+emp2+emp3))
# print((emp1+emp2+emp3).__repr__())
# print((emp1+emp2+emp3).__str__())
# print((emp1+emp2+emp3))

# print(emp1+emp2+1)

#
emp1=Employee(first="Gundu",last="Sarangi",pay=3000)
days_of_work=DaysOfwork(days=30)
print(days_of_work.days*emp1.pay)