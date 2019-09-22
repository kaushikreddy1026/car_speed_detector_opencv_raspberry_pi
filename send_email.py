#!/usr/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
def send_email(imageName):
    print("Sending Email")
    username = 'speeddetector101@gmail.com'
    password = 'LearnIOT06!'

    rcptlist = ['srinivassriram06@gmail.com', 'ssriram.78@gmail.com', 'abhisar.muz@gmail.com', 'raja.muz@gmail.com', 'mehtac@gmail.com', 'bhaskar.ambekar@gmail.com']
    receivers = ','.join(rcptlist)

    msg = MIMEMultipart('mixed')
    msg['Subject'] = 'From Chirayu\'s home - Speeding car in GVW'
    msg['From'] = username
    msg['To'] = receivers

    alternative = MIMEMultipart('alternative')
    textplain = MIMEText ('Captured a picture of a speeding car.')
    alternative.attach(textplain)	
    msg.attach(alternative)

    #jpeg_name = 'car_at_20190824_230024.jpg'
    #filename = '/home/pi/Downloads/git/carspeed/' + jpeg_name

    jpgpart = MIMEApplication(open(imageName, 'rb').read())
    jpgpart.add_header('Content-Disposition', 'attachment', filename=imageName)
    msg.attach(jpgpart)

    client = smtplib.SMTP()
    client = smtplib.SMTP('smtp.gmail.com', 587)
    client.starttls()
    client.login(username, password)
    client.sendmail(username, rcptlist, msg.as_string())
    print("Email Sent")
    client.quit()

