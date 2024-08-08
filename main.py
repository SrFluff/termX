import os
import files

def cls():

    os.system("clear")

root = ['2024']
ttf = ['august']
cd = root
pwd = '/'

main = True
menu = True

cls()

while main:

    while menu:

        a = input("|" + pwd + "|> ")
        if a == "ls":

            print("\n".join(cd))

        elif a == "exit":

            cls()
            exit()

        elif a == "clear":

            cls()

        elif a == "cd 2024" and cd == root:

            cd = ttf
            pwd = "/2024"

        elif a == "cd /":

            cd = root
            pwd = "/"

        elif a == "cd august" and cd == ttf:

            cd = files.aug
            pwd = "/2024/august"

        elif a == "cat 8" and cd == files.aug:

            print(files.eight)

        elif a == "cat 9" and cd == files.aug:

            print(files.nine)
