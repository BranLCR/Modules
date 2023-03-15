import smtplib

sender = "brandoncayamcela@gmail.com"
receiver = "NickBarnum@pm.me"
password = "password"
subject = "Python Email Test"
body = "This is an email sent using a python program :0"
#header
message = f"""From: Bran{sender}
To: {receiver}
Subject: {subject}
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
