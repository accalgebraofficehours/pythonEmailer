import smtplib

toaddrs = ["lviigurarie@gmail.com"]
fromaddrs = "adam.poodleschool.founder@gmail.com"
message = "Hi, I'm requesting you ."

numTimes = 200

with smtplib.SMTP("smtp.gmail.com", "587") as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login("adam.poodleschool.founder@gmail.com", "zlnzowjgeoalhwcj")
  for i in range(numTimes):
    smtpserver.sendmail(fromaddrs, toaddrs, message)
    print(i)

print("Done!")
