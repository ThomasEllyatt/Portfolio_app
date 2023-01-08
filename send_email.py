import smtplib
import os
from email.message import EmailMessage


def send_email(user_email, topic, message):
    host = "smtp.gmail.com"
    port = 465

    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = f"{topic} from {user_email}"
    msg['From'] = "Project Notifications <thomas.ellyatt@gmail.com>"
    msg['To'] = "thomas.ellyatt@gmail.com"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL(host, port)
    server.login(username, password)
    server.send_message(msg)
    server.quit()
