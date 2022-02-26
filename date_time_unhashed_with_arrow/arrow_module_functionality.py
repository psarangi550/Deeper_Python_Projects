import arrow

#converting to the arrow.utcnow() to fetch the current default time in utc default format
# print(arrow.utcnow())

#now we can also get the local time using the arrow.now() function which will provide local time but timezone enable 
# print(arrow.now())

##for formatting the code we can use as format() with the format code
# print(arrow.now().format())#this will provide isoformat code by default

##but if we want to use a particular format we can use it as format('<format_code>')
# print(arrow.now().format('MMMM DD YYYY'))


#now if we want the unix time we can use the timestamp() function as below
# print(arrow.utcnow().timestamp())


#now if we want to get the year/month/date then we can use it as below
# print(arrow.utcnow().year)
# print(arrow.utcnow().month)
# print(arrow.utcnow().day)


#arrow module uses shift instead of timedelta so we need to use it as below
# now=arrow.now()
# later=now.shift(hours=5)
# print(later.format('MMMM  DD YYYY hh:mm:ss a ZZ'))

#now by using the get() we can get the unix timestamp datetime 
#here the unix datetime can be priovided in the int/str format as below

# unix_timestamp_time=arrow.get(0)
# print(unix_timestamp_time.format('DD MMMM , YYYY'))

# unix_time_stamp=arrow.get(1234567890)
#here we are providing the unix timestamp datetime as str with the format code 
# unix_str_stamp=arrow.get('21/02/2022','DD/MM/YYYY')
# print(unix_time_stamp.format('DD MM YYYY'))
# print(unix_str_stamp.format('DD MM YYYY'))

##now we can select the range of hours/minutes/seconds as 
# now=arrow.now()
# later=now.shift(hours=7)

# for each in arrow.Arrow.range('hour',now,later): 
#     print(each.format('hh:mm:ss a ZZ'))


##here we can use any time zone as args inside the now() but not in utcnow()
# print(arrow.now('US/Mountain'))