import os
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import mimetypes
from email.mime.multipart import MIMEMultipart

def sendEmail(email_address, email_body, email_attachments):
    
    msg = MIMEMultipart()
    msg['To'] = email_address
    msg['From'] = email_address
    msg['Subject'] = "Test Email"
    text_msg = MIMEText(email_body, 'plain')
    msg.attach(text_msg)
    for attachment in email_attachments:
        ctype, encoding = mimetypes.guess_type(attachment)
        maintype, subtype = ctype.split("/",1)
        if maintype == "image":
            fp = open(attachment, 'rb')
            file = MIMEImage(fp.read())
            fp.close()
        elif maintype == "text":
            fp = open(attachment)
            file = MIMEText(fp.read())
            fp.close()
        elif maintype == "audio":
            fp = open(attachment, 'rb')
            file = MIMEAudio(fp.read())
            fp.close()
        else:
            fp = open(attachment, 'rb')
            file = MIMEBase(fp.read())
            fp.close()
        file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
        msg.attach(file)
    
    return msg

if __name__ == "__main__":
    email_address = "eddie.valv@gmail.com"
    body = "Text for the email body"
    attachments = ['v:/workspace/Email_Homework/src/python-logo.png', 'v:/workspace/Email_Homework/src/Text.txt']
    output = sendEmail(email_address, body, attachments)
    print(output)