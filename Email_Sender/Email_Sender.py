# to get this code to run, you will need to create a file called app2.py,
# inside this file, create variables called email and password and set the values to that of the sender G-mail account
# and a password generated from google account app password generator
from email.message import EmailMessage
from app2 import email  # create 2nd file and store email as variable for security
from app2 import password  # store password in created file as variable for security
import ssl
import smtplib

email_sender = email
email_password = password

email_reciever = ['', '', '']  # enter recipient email

subject = 'Testing our python skills'
body = """ 
We're just testing our python skills, by setting up an email sender.

this text should be on multiple lines!
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
