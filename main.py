import os

def cls():

    os.system("clear")

root = ['2024']
ttf = ['august']
aug = ['8.txt']
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

        elif a == "cd 2024" and cd == root:

            cd = ttf
            pwd = "/2024"

        elif a == "cd /":

            cd = root
            pwd = "/"

        elif a == "cd august" and cd == ttf:

            cd = aug
            pwd = "/2024/august"

        elif a == "cat 8" and cd == aug:

            print("First log, you should get")
            print("some sleep buddy. You can")
            print("upload and finish :)")
