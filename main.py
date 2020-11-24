import smtplib
import os
from email.message import EmailMessage
import imghdr

EMAIL_USER = "knockknockcis3296@gmail.com"
EMAIL_PASSWORD = "Cis3296!"

msg = EmailMessage()
msg['Subject'] = 'Delivery detected'
msg['From'] = EMAIL_USER
msg['To'] = 'tug84792@temple.edu'
msg.set_content('A package has been delivered at your door from (EXACT TYPE OF COURIER)')

with open('test.jpg','rb') as f:
	file_data = f.read()
	file_type = imghdr.what(f.name)
	file_name = f.name
	#print(file_type)

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name)

# with open('test.jpg','rb') as f:
# 	file_data2 = f.read()
# 	file_type2 = imghdr.what(f.name)
# 	file_name2 = f.name
# 	#print(file_type)
#
# msg.add_attachment(file_data2, maintype='image', subtype=file_type2, filename = file_name2)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_USER, EMAIL_PASSWORD)
	smtp.send_message(msg)
