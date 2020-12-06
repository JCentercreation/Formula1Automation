import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emaildelivery():
    mailadress = ''
    mailpassword = ''
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(mailadress, mailpassword)

    file = open("Mensaje.txt", "r")
    messagestorage = []
    for l in file:
        messagestorage.append(l)
    file.close()

    file = open("Mensaje.txt", "r")
    msg = MIMEMultipart()
    msg['From'] = mailadress
    msg['To'] = ''
    msg['Subject'] = str(messagestorage[0])
    message = file.read()
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()
    file.close()