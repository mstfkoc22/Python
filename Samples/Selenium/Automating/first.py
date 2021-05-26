import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

sender = 'sender@gmail.com'
receiver = 'receiver@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'New Jobs on Indeed'
msg['From'] = sender
msg['To'] = ','.join(receiver)

part = MIMEBase('application', 'octet-stream')
part.set_payload(open('C:/Coding/Python/jobs.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="jobs.csv"')
msg.attach(part)

s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'sender@gmail.com', password= 'password')
s.sendmail(sender, receiver, msg.as_string())
s.quit()