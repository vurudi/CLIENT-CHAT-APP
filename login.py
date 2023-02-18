import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def login():
    # login button
    with open('logemail.txt', 'r') as f:
        login_email = f.read()

        if login_email == '':
            # reg button
            register()
        else:
            inputpass = "pass"

            with open('logpassword.txt', 'r') as f:
                login_password = f.read()
            if inputpass == login_password:
                main_page()
            else:
                pass
    # retore button
    restorepass = True
    if restorepass:
        pass_reset()


def pass_reset(sender, recipient):
    """ Send password  """

    msg = MIMEMultipart()
    msg['Subject'] = 'vurudi100 msg 1 verify'
    msg['To'] = recipient
    msg['From'] = sender
    subject = 'VURUDI100 SOFTWARE SPOT!'
    # attach image files
    otp = random(100000, 900000)
    with open('logpassword.txt', 'r') as f:
        restoredpass = f.read()
        retrived_password = 'Your recovered password is ' + restoredpass
    msg.attach(MIMEText(retrived_password, 'plain'))

    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    with open('se_pass.txt', 'r') as f:
        password = f.read()
    session.login(sender, password)
    session.sendmail(sender, recipient, msg)
    print("Email sent.")
    session.quit()


def register():
    firstName = 'name'
    secondName = 'name2'
    emailadress = ''
    nickname = 'nickname'
    prefaredpass = 'prpass'

    if emailadress == '' or firstName == '' or secondName == '' or nickname == '' or prefaredpass == '':
        register()
    else:
        with open('serveremail.txt', 'r') as f:
            servemail = f.read()
        email(servemail, emailadress, firstName)

        with open('firstname.txt', 'w') as f:
            f.write(firstName)

        with open('secname.txt', 'w') as f:
            f.write(secondName)

        with open('logemail.txt', 'w') as f:
            f.write(emailadress)

        with open('nickname.txt', 'w') as f:
            f.write(nickname)

        with open('logpassword.txt', 'w') as f:
            f.write(prefaredpass)
        login()


def main_page():
    print(35456)
    pass


def email(sender, recipient):
    """ Send email message """
    username = 'domi'
    msg = MIMEMultipart()
    msg['Subject'] = 'vurudi100 msg 1 verify'
    msg['To'] = recipient
    msg['From'] = sender
    subject = 'VURUDI100 SOFTWARE SPOT!'
    # attach image files
    otp = random(100000, 900000)
    with open('messege1.txt', 'r') as f:
        messege = f.read()
        messege = 'Hello' + username + messege + f'Your OTP is   {otp}'
    msg.attach(MIMEText(messege, 'plain'))

    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    with open('gmaillogpass.txt', 'r') as f:
        password = f.read()
    session.login(sender, password)
    session.sendmail(sender, recipient, msg)
    print("Email sent.")
    session.quit()


def approval_mail(sender, recipient):
    """ Send email message """
    msg = MIMEMultipart()
    msg['Subject'] = 'Account Creation was successfull'
    msg['To'] = recipient
    msg['From'] = sender
    subject = 'VURUDI100 SOFTWARE SPOT!'
    # attach image files
    otp = 889
    with open('messege.txt', 'r') as f:
        messege = f.read()
        messege = messege + f'{otp} paxpaxpax100@gmail.com'
    msg.attach(MIMEText(messege, 'plain'))
    filename = 'vurudi100.jpg'
    attachment = open(filename, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(p)
    text = msg.as_string()

    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    with open('gmaillogpass.txt', 'r') as f:
        password = f.read()
    session.login(sender, password)
    session.sendmail(sender, recipient, text)
    print("Email sent.")
    session.quit()

class Filetrancfar:
    def sendfile(name):
        s = socket.socket()
        host = "192.168.56.1"
        port = 5001
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected to ", host)
        filename = name  # SENDING MODULE
        filesize = os.path.getsize(filename)
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        # file = open(filename, 'wb')

        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True,
                             unit_divisor=1024)
        with open(filename, "rb") as f:
            tim = 0
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))
        print("file shared succesfully")
        s.close()


if __name__ == '__main__':
    sn = 'vurudi100@gmail.com'
    rec = 'paxpaxpax100@gmail.com'
    email(sn, rec)
