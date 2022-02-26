import datetime
import pytz
# print(datetime.date.today())
# print(datetime.datetime.today())

#no aware as its only local naive time
# print(datetime.datetime.today(tz_info=None))###error####
#naive_time
# print(datetime.time(hour=17,minute=00,tzinfo=None))##UTC NOT AWARE
#naive_time
# print(datetime.datetime.utcnow())##UTC NOT AWARE
#aware_time
# print(datetime.datetime.now(tz=pytz.UTC))#UTC AWARE 
#aware_time
# print(datetime.time(hour=17,minute=00,tzinfo=pytz.UTC))#UTC AWARE
#aware_time
# print(datetime.datetime(year=2022,month=2,day=24,hour=17,minute=00,tzinfo=pytz.UTC))#UTC AWARE
#aware_time
# print(datetime.datetime.utcnow().replace(tzinfo=pytz.UTC))##UTC AWARE
#aware_time
# print(datetime.datetime.today().replace(tzinfo=pytz.UTC))##UTC AWARE

#fetch_all_timezone
# for timezone in pytz.all_timezones:
#     print(timezone)
