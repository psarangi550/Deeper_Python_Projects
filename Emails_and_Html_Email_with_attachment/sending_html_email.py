import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = 'pratik.corey@gmail.com'
EMAIL_PASSWORD=os.getenv('email_pass')

msg=EmailMessage()
msg['Subject']='Hello There'
msg['from']=EMAIL_ADDRESS
msg['to']='pratik.corey@gmail.com'
msg.set_content('This is a Test Html Email Message')
msg.add_alternative('''
                   <!DOCTYPE html>
                   <html lang="en">

                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                    </head>

                    <body>
                        <h1>Hello There this is a Test Email</h1>
                    </body>

                    </html> 
                    ''',subtype='html')


with smtplib.SMTP('smtp.gmail.com',587) as smtp: 
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)