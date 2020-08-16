import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

banner = """
   _______________          _______________
  |  ___________  |        |  ___________  |
  | |           | |        | |           | |
  | |   X   X   | |        | |           | |
  | |     -     | |        | |   0   0   | |
  | |    ___    | |        | |     -     | |
  | |   /   \   | |        | |   \___/   | |
  | |   \___/   | |        | |           | |
  | |___________| |        | |___________| |
  |_______________|        |_______________|
    ____|   |___.............._|________|_
   | ********** |            | ********** |
   | ********** |            | ********** |
    ------------              ------------
   [ Coded by : erfan4lx] Teams : [M4nifest0 - Unidentified - Vortex ](Cyber Security Teams)
"""

print(banner)

def main(emailf, password, host, port, emailt, subject, message):
    s = smtplib.SMTP(host=str(host), port=int(port))
    s.starttls()
    s.login(str(emailf), str(password))
    msg = MIMEMultipart()
    msg['From']=str(emailf)
    msg['To']=str(emailt)
    msg['Subject']=str(subject)
    msg.attach(MIMEText(str(message), "plain"))
    s.send_message(msg)
    s.quit()
    del msg

f1 = open("emailsf.txt","r").read()
f2 = open("passwords.txt","r").read()
f3 = open("hosts.txt","r").read()
f4 = open("ports.txt","r").read()
f5 = open("emailst.txt","r").read()
f10 = open("subtext.txt","r").read()
f10 = f10.split()
f6 = f10[0]
f7 = f10[1]
f1 = f1.split()
f2 = f2.split()
f3 = f3.split()
f4 = f4.split()
f5 = f5.split()

c = 0
counter = 0

count = input("Counter: ")

for i in f5:
    try:
        if counter == count:
            c += 1
        main(f1[c],f2[c],f3[c],f4[c],i,f6,f7)
        counter += 1
    except:
        print(banner)
        sys.exit()
