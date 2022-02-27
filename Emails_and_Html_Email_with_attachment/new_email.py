import smtplib
import os

EMAIL_ADDRESS = 'pratik.corey@gmail.com'
EMAIL_PASSWORD=os.getenv('email_pass')

with smtplib.SMTP('smtp.gmail.com',587) as smtp: 
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    subject='Hello There'
    body='This is a Test Email Message'
    msg=f'Subject:{subject} \n\n\n {body}'
    smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)

# print(os.getenv('email_pass'))
