import smtplib

msg='Test321'
subject='Test'
from_name='TreM'
to_name='Trev'
from_addr = 'tmurray531@gmail.com'
to_addr = 'tre-20@hotmail.com'
message = """
From: 'tmurray531@gmail.com'
To: 'tre-20@hotmail.com' 
Subject: 'Testing 123'
"""
msg='Email test'

message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)
# Credentials (if needed)
username = ' '
password = ' '
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 