import csv


#python 2 script so need not to be worry about 

with open('data.csv','w') as f: #
    csv_writter=csv.writer(f)
    csv_writter.writerow(['eno','ename','esal','eaddr'])
    while True:
        eno=int(raw_input("Enter Your Employee Number"))
        ename=raw_input("Enter your Name")
        esal=float(raw_input("Enter your Salary"))
        eaddr=raw_input("Enter your Address")
        csv_writter.writerow([eno,ename,esal,eaddr])
        option=raw_input("Do you wish to add more record [y/n]: ")
        if option.lower()=="n":
            print ("Records been updated")
            break
        
        