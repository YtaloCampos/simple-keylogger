from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# send email
def send_email(arguments):

  #read file
  f = open("tmp/log.txt", "r")

  # create message object
  msg = MIMEMultipart()

  # read file log
  message = f.read()

  # setup the parameters of the message
  password = arguments[2]
  msg['From'] = arguments[0]
  msg['To'] = arguments[1]
  msg['Subject'] = 'log information'

  # add in the message body
  msg.attach(MIMEText(message, 'plain'))

  #create server
  server = smtplib.SMTP('smtp.gmail.com: 587')

  server.starttls()

  # Login Credentials for sending the mail
  server.login(msg['From'], password)

  # send the message
  server.sendmail(msg['From'], msg['To'], msg.as_string())

  server.quit()

  print("Email sended to:", arguments[1])
  exit()