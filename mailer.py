import smtplib
from email.mime.text import MIMEText
import socket


def send_email(to, subject, body, sender,password ):

    message = MIMEText(body,'html')
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = to

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) # Change this to your email server and port
        server.starttls()
        server.login(sender, password)
        server.send_message(message)
        server.quit()
        return True
    except smtplib.SMTPException as e:
        print(f"Error: Unable to send email to {to}")
        print(e)
        return False
    except socket.gaierror as e:
        print(f"Error: Could not connect to email server for {to}")
        print(e)
        return False
    except socket.error as e:
        print(f"Error: Could not send email to {to}")
        print(e)
        return False