import faker
import random
import uuid
import string

#Integrating the random with the uuid
# num1=random.seed(3)
# num2=random.randint(1,1000000000000000000000)
# print(num2)

# uuid1=uuid.UUID(int=num2)
# print(uuid1)
# # print(uuid1.hex)
# str1=str(uuid1)
# print(uuid.UUID(str1))

#integrating the faker with the uuid

fake=faker.Faker()#using the Faker module to create a fake object
# print(dir(fake))
num=faker.Faker.seed(8786)
print(fake.name())
# print(num)
name1=fake.name().split()[0]
print(type(name1))
print(name1)
# print(fake.uuid4())
# UUID2=uuid.UUID(name1)
# print(UUID2)