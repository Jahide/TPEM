

user=input("Please enter your username :- ")
email=input("Please enter your email address :-")
email1=input("Please enter your confirm email:- ")
if email!=email1:
  email1=input("please enter your correct Email :- ")
password=input("Please enter your new password :- ")
pass1=input("Please enter your confirm password :- ")
if password!=pass1:
  pass1=input("Please enter your confirm password :- ")

else:
  print("successfully created your account")

if password==pass1:
  print("username           - ",user)
  print("your email address - ",email1)
  print("your password      - ",pass1)
