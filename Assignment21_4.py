import psutil
import os
import smtplib
from email.message import EmailMessage


def send_mail(mail,path):
    sender_email = "inamdararmaan2@gmail.com"
    receiver_email = mail
    subject = "Running processes information file"
    password = "cfzhjakehqunucqo"

    attachment_path = path

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content("""\
        Hello,

        This email contains a list of currently running processes on the system.

        Regards,
        Armaan (Python script)
        """)


    fobj = open(attachment_path, 'rb')
    file_data = attachment_path.read()
    file_name = os.path.basename(attachment_path)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

def processdisplay(name):
    ret = os.path.isabs(name)
    if(ret == False):
        name = os.path.abspath(name)

    filename = os.path.join(name,"log.txt")
    
    fobj = open(filename,'w')

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name'])
        user = proc.username()
        fobj.write(str(info))
        fobj.write("user : "+user)
        fobj.write("\n")

    return filename


def main():
    print("Enter directory name :")
    name = input()
    print("Enter mail id :")
    mail = input()
    path = processdisplay(name)
    send_mail(mail,path)

if __name__ == "__main__":
    main()