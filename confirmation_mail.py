import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_address = "Enter sender email here"
sender_pass = "Enter sender password here"
recipients_address = "Enter Recipients email here"
subject = " Model Trained "
content = '''Hey, 
			 Your model has been trained and desired accuracy is achieved.
			'''
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = recipients_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('Enter your SMTP host', 2525)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, recipients_address , text)
session.quit()
print('Mail Sent...')
