import smtplib

sender_email = "example123@gmail.com"
receiver_email = "receiver@gmail.com"
app_password = "your password"

subject = "Test Mail"
message = "Hello! Mail sent using Python."

text = f"Subject: {subject}\n\n{message}"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender_email, app_password)

    server.sendmail(sender_email, receiver_email, text)

    print("Mail Sent Successfully")

    server.quit()

except Exception as e:
    print("Error :", e)
