simport smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


sender_email = "example123@gmail.com"
receiver_email = "receiver@gmail.com"
app_password = "your password"


msg = MIMEMultipart()

msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "File Attachment"


body = "Hello, this is a file attachment email."

msg.attach(MIMEText(body, "plain"))


filename = "C:/Users/C2C.ITPG19/Documents/New folder/errordisplay.py"

attachment = open(filename, "rb")

part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

msg.attach(part)


server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(sender_email, app_password)

server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email Sent Successfully!")

server.quit()
