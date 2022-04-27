import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email_html_body import html_body
import requests

print("Initiating the bot...\n")

#API GitHub (json format required)
response = requests.get("https://api.github.com/users/LuizHB")
data = response.json()

#your email
fromaddr = "examplesender@mail.com"
#emails to send
toaddr = "exampletarget1@mail.com, exampletarget2@mail.com"

#MIMEMultipart Instance

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test email with HTML and API GitHub plus attachment"
body = "Followers: %s\n Following: %s \n" % (data['followers'],data['following'])

#external body with html
body1 = MIMEText(html_body,"html")

#plain body inside code
body2 = MIMEText(body,'plain')

#attach messages on the email
msg.attach(body1)
msg.attach(body2)

#Attachment
filename = "sample.pdf"
attchfile = open("sample.pdf","rb")
p = MIMEBase('application', 'octet-stream')

p.set_payload((attchfile).read())

#encode the file for base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

#attach the file on the email
msg.attach(p)

#Server SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

#Security
s.starttls()

# login (add password between ' ')
s.login(fromaddr, '123456')

#convert to string
text = msg.as_string()

#send email
s.sendmail(fromaddr,toaddr, text)

print("Emails sent to %s" % toaddr)
s.quit()

