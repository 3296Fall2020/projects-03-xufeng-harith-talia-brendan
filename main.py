import os
import smtplib
from email.message import EmailMessage
import imghdr
from email.mime.text import MIMEText

from fpdf import FPDF

EMAIL_USER = "knockknockcis3296@gmail.com"
EMAIL_PASSWORD = "Cis3296!"

msg = EmailMessage()
msg['Subject'] = 'Delivery detected'
msg['From'] = EMAIL_USER
msg['To'] = 'tug84792@temple.edu'
msg.set_content('A package has been delivered at your door from (EXACT TYPE OF COURIER)')

#Section to convert a text file to a pdf
#======================================================================#
def txtToPDF(txtFile):

	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 10)

	f = open(txtFile, "r")
	for i in f:
		pdf.cell(0,txt = i, ln = 1)

	return pdf.output("sampleFile.pdf")

txtFile= "/Users/harith.siddiqui754/PycharmProjects/kkEmail/sampleFile.txt"
txtToPDF(txtFile)
#=======================================================================#

#Section to send an email
#=======================================================================#

#This section attaches an image to the email
def attachImage(filePath):
	with open(filePath, 'rb') as f:
		file_data = f.read()
		file_type = imghdr.what(f.name)
		file_name = f.name
	msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
def sendIMG(filePath):
	attachImage(filePath)
sendIMG('test.jpg')

#Attaches the pdf
def attachPDF(filePath):
	with open(filePath,'rb') as f:
		file_data = f.read()
		file_name = f.name
	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)

def sendPDF(filePath):
	attachPDF(filePath)
sendPDF('sampleFile.pdf')

"""# Create an object of sendpdf function  
k = sendpdf(sender_email_address,  
            receiver_email_address, 
            sender_email_password, 
            subject_of_email, 
            body_of_email, 
            filename, 
            location_of_file) 
  
# sending an email 
k.email_send()"""
#msg.attach(MIMEText(open("sampleFile.pdf").read()))
# with open('test.jpg','rb') as f:
# 	file_data = f.read()
# msg.add_attachment(file_data)

# with open('test.jpg','rb') as f:
# 	file_data2 = f.read()
# 	file_type2 = imghdr.what(f.name)
# 	file_name2 = f.name
# 	#print(file_type)
#
# msg.add_attachment(file_data2, maintype='image', subtype=file_type2, filename = file_name2)
attachImage('test.jpg')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_USER, EMAIL_PASSWORD)
	smtp.send_message(msg)
#=======================================================================#
