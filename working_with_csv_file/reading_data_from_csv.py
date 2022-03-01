import csv
from tabulate import tabulate
result_var1=[]
def main():
    with open('data.csv','r') as f: #
        csv_reader=csv.reader(f)
    # print(type(csv_reader))
    # print(dir(csv_reader))
        for row in csv_reader:
        # print(tabulate(row))
            result_var1.append(row)
        # print()
        
        # result.append(row)

main()
            
result_var=result_var1[1:]
# print(result_var)
print(tabulate((result_var),headers=["eno","ename","esal","eaddr"]))
          
    # for record in result[1:]: #
    #     print(record)
    #     # print(tabulate(record))
    #     # print(f"Emp No {record[0]}")
    #     # print(f"Emp Name {record[1]}")
    #     # print(f"Emp sal {record[2]}")
    #     # print(f"Emp address {record[3]}")
    #     print()

# print(result)

if __name__ == "__main__":
    main()
