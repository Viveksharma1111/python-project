import os
print("\n\t\t\tWORLD OF AOUTOMATION")
while True:
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("\n\t\t\tHOW CAN I HELP YOU")
    print("""\noption 1 : Groot please run date command for me
               option 2 : Groot please run cal command for me
               option 3 : Groot please cheak my ip
               option 4 : Groot please open my browser
               option 5 : Groot please open maual for cal
               option 6 : Groot please show my all directory
               option 7 : Groot please show my current dirctory
               option 8 : Groot please run help command for me 
               option 9 : Groot please exit""")
    order=int(input("Give me order:"))           
    if order==1:
        date=os.system("date")
        print(date)
    elif order==2:
        cal=os.system("cal")
        print(cal)
    elif order==3:
        ip=os.system("ifconfig")
        print(ip)
    elif order==4:
        firefox=os.system("firefox")
        print(firefox)
    elif order==5:
        maual=os.system("man cal")
        print(maual)
    elif order==6:
        dir=os.system("dir")
        print(dir)
    elif order==7:
        pwd=os.system("pwd")
        print(pwd)
    elif order==8:
        help=os.system("help")
        print(help)                           
    elif order==9:
        exit=os.system("exit")
        print(exit)
        break
    #else:
     #   print("Please enter valid input")