import pyfiglet
from termcolor import colored
nu="pradip"
pas="pradip"
p7=8
e4="o"
title=colored("Wclocome to  login page",'green')
center_title=title.center(40)
print(center_title)
us=input(colored("Enter username :",'yellow'))
if us==nu:
  password=input(colored("Enter Password:",'yellow'))
  if password==pas:
   print(colored("Successfully login",'green'))
   banner = pyfiglet.figlet_format("💛I LOVE YOU ELILO Z ODYUO💖", font = "digital")
   print(banner)
  else:
    print(colored("Sorry Wrong Password",'red'))
    on=input("do you want to found password Y/N ? ")
    if on=="Y":
      ls=[]
      ls1=input("Enter 1 Eord")
      ls2=input("Enter 2 Word")
      ls3=input("Enter 2 Word")
      ls4=input("Enter 3 Word")
      ls5=input("Enter 5 Word")
      ls.append(ls1)
      ls.append(ls2)
      ls.append(ls3)
      ls.append(ls4)
      ls.append(ls5)
      for mol in ls:
        if mol==nu:
          print(f"username found  :- {mol}")
          if ls==pas:
            us=input("Enter username :")
          if us==nu:
            ss=input("Enter Password:")
          if ss==pas:
            print("Successfully login")
            banner = pyfiglet.figlet_format("💖I LOVE YOU ELILO Z ODYUO💛")
            print(banner)
else:
  print(colored("Sorry Wrong username",'red'))
  cl=input(colored("Enter Y if You Want Boots Force",'blue'))
  cl2="Y"
  cl3="N"
  if cl==cl2:
    ls=[]
    ls1=input("Enter 1 Eord")
    ls2=input("Enter 2 Word")
    ls3=input("Enter 2 Word")
    ls4=input("Enter 3 Word")
    ls5=input("Enter 5 Word")
    ls.append(ls1)
    ls.append(ls2)
    ls.append(ls3)
    ls.append(ls4)
    ls.append(ls5)
    for msl in ls:
      if msl==nu:
        print(f"username found  :- {msl}")
  if cl==cl3:
    print("thenk")
  if  cl==cl2:
    prs=input("do you want to found password Y/N ? ")
    w1="Y"
    w2="N"
    if prs==w1:
       ls=[]
       ls1=input("Enter 1 word")
       ls2=input("Enter 2 word")
       ls3=input("Enter 2 word")
       ls4=input("Enter 3 word")
       ls5=input("Enter 5 Word")
       ls.append(ls1)
       ls.append(ls2)
       ls.append(ls3)
       ls.append(ls4)
       ls.append(ls5)
       for mo in ls:
         if mo==pas:
           mn=print(f"Password found :- {mo}")
       else:
         print(colored ("Done 💖💛",'red'))
    if prs==w2:
      print("Thank you")
    e4=input("login Y/N")
    p7="Y"
if e4==p7:
        us=input("Enter username :")
        if us==nu:
          ss=input("Enter Password:")
        if ss==pas:
          print("Successfully login")
          banner = pyfiglet.figlet_format("I LOVE YOU ELILO Z ODYUO")
          print(banner)
