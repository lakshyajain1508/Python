import smtplib

sender = "lakshyajain1508@gmail.com"
recipient = "lakshyajain1508@gmail.com"
password = "vwjbxacycwdzsrym"

message = """
Subject: Test Email from Python
Hello Lakshya,
This is a test email sent from a Python script using the smtplib library.
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, recipient, message)
server.quit()

print("✅ Email sent successfully!")