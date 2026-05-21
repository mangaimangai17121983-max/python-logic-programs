import smtplib

sender_email = "mangaimangai17121983@gmail.com"
receiver_email = "rayeesaiffath@gmail.com"
app_password = "kcyy hgfd yavk avrr"

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
