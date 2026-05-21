import smtplib
import time
from email.mime.text import MIMEText

current_time = time.strftime("%H:%M:%S")

sender_email = "mangaimangai17121983@gmail.com"
receiver_email = "rayeesaiffath@gmail.com"
app_password = "kcyy hgfd yavk avrr"

subject = "Current Time"
body = "Current Time is: " + current_time

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, app_password)

server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email Sent Successfully!")

server.quit()
