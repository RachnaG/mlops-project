import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "19ee3e2137d7f1"
host_pass = "61df57bfaa2a04"
guest_address = "rachnakgupta81@gmail.com"
subject = "Regarding failure of rebuild.py"
content = '''Hello, 
				Developer is in the last commit regarding error . it is rebuild agin
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.mailtrap.io', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
