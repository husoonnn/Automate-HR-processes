#Run `pip install -r requirements.txt`

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import csv

from pip import main


def send_email(subjectname, company, typeofplan, receiver_email):
    print("Current subjectname:", subjectname)
    subject = "Congratulations on the Grant of {company} {typeofplan}, {subjectname}!".format(company=company, typeofplan=typeofplan, subjectname=subjectname)
    
    body = '''
    {subjectname}, 

     {company}. 

   '''.format(company=company, subjectname=subjectname)
    
    receiver_email = receiver_email
    filename = "{subjectname}.pdf".format(subjectname=subjectname)  # In same directory as script


    sender_email = #input email
    password = #input secured key from service provider: Gmail/yahoo/etc

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("gmail.com", 465, context=context) as server:
        #server.set_debuglevel(1)
        #server.ehlo()
        server.login(sender_email, password)
        #server.ehlo()
        server.sendmail(sender_email, receiver_email, text)


if __name__ == '__main__':
    file = open('sample.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    subjectname = []
    company = []
    typeofplan = [] 
    receiver_email = []
    for row in csvreader:
        subjectname.append(row[0])
        company.append(row[1])
        typeofplan.append(row[2])
        receiver_email.append(row[3])

    for i in range(1, len(subjectname)):
        send_email(subjectname[i], company[i], typeofplan[i], receiver_email[i])
