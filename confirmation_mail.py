import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "05833dfff32054"
host_pass = "fc875e30b60d71"
guest_address = "sagargarg272@gmail.com"
subject = " Model Trained "
content = '''Hey, 
				Your model has been trained and desired accuracy is achieved.
			'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.mailtrap.io', 2525)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Mail Sent...')
