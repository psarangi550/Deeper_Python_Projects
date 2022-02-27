import smtplib
from email.message import EmailMessage
import os
import imghdr

# print(imghdr.what('abi.jpeg'))

EMAIL_ADDRESS = 'pratik.corey@gmail.com'
EMAIL_PASSWORD=os.getenv('email_pass')

msg=EmailMessage()
msg['Subject']='Hello There'
msg['from']=EMAIL_ADDRESS
msg['to']='pratik.corey@gmail.com'
msg.set_content('This is a Test Html Email Message')

with open('abi.jpeg','rb') as f: 
    file_data=f.read() 
    file_type=imghdr.what(f.name)
    file_name=f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    
with smtplib.SMTP('smtp.gmail.com',587) as smtp: 
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)