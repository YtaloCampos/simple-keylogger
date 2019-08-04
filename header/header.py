import time

def header():
    main = """
      _____     _      ____     _          ____       _____
     / ____|   | |    / ___|   | |        / __ \     / ____|
    / /        | |   / /       | |       / /  \ \   / /
    \ \___     | |   \ \__     | |      | |    | |  | |   ___
     \___ \    | |    \__  \   | |      | |    | |  | |  |_  |
         \ \   | |        \ \  | |      | |    | |  | |    | |
     ____/ /   | |    ____/ /  | |____   \ \__/ /   \ \___/ /
    |_____/    |_|   |_____/   |______|   \____/     \_____/


                                                Powered by Ytalo Campos.""" 

    print(main)
    time.sleep(2)         

    print("--from - sender email")
    print("--to - recipient email")
    print("--pass - sender password\n")
    time.sleep(1)

    print("> press 'F4' to receive the data by email")
    print("> press 'ESC' to close\n")
    print("loading...")
