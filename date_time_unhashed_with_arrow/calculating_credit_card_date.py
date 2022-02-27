import datetime
import calendar

balance=5000
interest=12*0.01
monthly_payment=500 

print(balance)

tday=datetime.date.today()
# print(tday)
cal_month_range=calendar.monthrange(tday.year,tday.month)[1]
# print(type(cal_month_range))#(0,28)

date_until_next=tday+datetime.timedelta(days=(cal_month_range-tday.day)+1)
# print(date_until_next)#2022-03-01

end_date=date_until_next

while balance > 0: #
    interest_bal=balance*(interest/12)
    balance+=interest_bal
    balance-=monthly_payment
    
    balance =round(balance,2)
    if balance < 0: 
        balance=0 #
    
    date_untill=calendar.monthrange(end_date.year,end_date.month)[1]
    end_date=end_date+datetime.timedelta(days=(date_untill-end_date.day)+1)
    print(f'{end_date}----->{balance}')
    
    
