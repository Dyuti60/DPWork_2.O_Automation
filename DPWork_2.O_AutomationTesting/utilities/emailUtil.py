# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from exception import CustomException
import pandas as pd
import os
import sys

def sendEmail(sender,emailsenderpassword,receiversTo,receiversCC, evidence_attachment, report_attachment):
    try:
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        # storing the senders email address
        msg['From'] = sender
        # storing the receivers email address
        msg['To'] = str(receiversTo)
        msg['Cc'] = str(receiversCC)
        #date when email sent
        date_str=pd.Timestamp.today().strftime('%d-%m-%Y')
        # storing the subject
        msg['Subject'] = f'DP Work Portal Automation Testing : Login Functionality - {date_str}'
        # string to store the body of the mail
        body = '''
        <p>
        Joyguru Team,</br></br>
        Greetings !!
        We have successfully validated login page functionality.
        Please go through the attachments.
        </br></br>
        Regards,</br>
        DP Works Portal Automation, Jorhat,</br>
        Assam,</br>
        </p>
        '''
        #.format(str(googledrivepath))
        # attach the body with the msg instance
        #msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(body, 'html'))


        # open the file to be sent
        attachment1 = open(evidence_attachment, "rb")
        # instance of MIMEBase and named as p1
        p1 = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        p1.set_payload((attachment1).read())
        # encode into base64
        encoders.encode_base64(p1)
        string=evidence_attachment
        filename1=string.split('\\')[-1]
        p1.add_header('Content-Disposition', "attachment1; filename= %s" % filename1)
        # attach the instance 'p1' to instance 'msg'
        msg.attach(p1)

        # open the file to be sent
        attachment2 = open(report_attachment, "rb")
        # instance of MIMEBase and named as p2
        p2 = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        p2.set_payload((attachment2).read())
        # encode into base64
        encoders.encode_base64(p2)
        string=report_attachment
        filename2=string.split('\\')[-1]
        p2.add_header('Content-Disposition', "attachment2; filename= %s" % filename2)
        # attach the instance 'p2' to instance 'msg'
        msg.attach(p2)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(sender, emailsenderpassword)
        # Converts the Multipart msg into a string
        text = msg.as_string()
        # sending the mail
        s.sendmail(sender, msg['To'].split(";")+msg['Cc'].split(";"), text)
        # terminating the session
        s.quit()
    except Exception as e:
        raise CustomException(e,sys)
