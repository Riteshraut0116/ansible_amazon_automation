import smtplib
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(email, file_path):
    from_email = os.getenv("EMAIL_ADDRESS")
    from_password = os.getenv("EMAIL_PASSWORD")
    to_email = email

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Dell Laptops List"

    part = MIMEBase('application', 'octet-stream')
    with open(file_path, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="dell_laptops.xlsx"')
    msg.attach(part)

    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.starttls()
    mail_server.login(from_email, from_password)
    mail_server.sendmail(from_email, to_email, msg.as_string())
    mail_server.quit()

if __name__ == "__main__":
    email = sys.argv[1]
    file_path = sys.argv[2]
    send_email(email, file_path)
