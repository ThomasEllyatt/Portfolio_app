import smtplib
import ssl
from email.message import EmailMessage


def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 465

    username = "thomas.ellyatt@gmail.com"
    password = "buookdhcjicjguzg"

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = f"You have a new email from {user_email}"
    msg['From'] = "NEW bigquery_notifications <thomas.ellyatt@gmail.com>"
    msg['To'] = "thomas.ellyatt@gmail.com"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL(host, port)
    server.login(username, password)
    server.send_message(msg)
    server.quit()
