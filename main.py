import os
import smtplib
from email.message import EmailMessage
import imghdr
from email.mime.text import MIMEText
import cv2
import numpy as np
import time
import darknet
from setEmail import email
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
def txtToPDF(filePath):

	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 10)

	f = open(filePath, "r")
	for i in f:
		pdf.cell(0,txt = i, ln = 1)

	return pdf.output("output.pdf")

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
#sendIMG('test.jpg')

#Attaches the pdf
def attachPDF(filePath):
	with open(filePath,'rb') as f:
		file_data = f.read()
		file_name = f.name
	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)

def sendPDF(filePath):
	attachPDF(filePath)
#sendPDF('sampleFile.pdf')

def sendAttachments(imgPath, pdfPath):
	sendIMG(imgPath)
	#newPDF = txtToPDF(pdfPath)
	sendPDF(pdfPath)

sendAttachments('test.jpg', 'output.pdf')


############################
#write detections to log file
############################




#################################################
#Rules to decide if an detected object is valid
#rule 1: confident bigger or equal to 85%?
#rule 2: 
#################################################




##################################
#The main part
##################################
def main():
    #perform detection
    configPath = "./cfg/knockknock_cfg.cfg"
    weightPath = "./knockknock_cfg_best.weights"
    metaPath = "./cfg/obj.data"
    
    #decide input source
    cap = cv2.VideoCapture("")#<-enter input video address here    
    RTSP_URL = #enter RTSP URL here if using a camear
    cap = cv2.VedeoCapture(RTSP_URL)
    
    #set output video footage
    
    #a reuse image for each detection
    
    #loop through the video
        #a detection go through the rule
        #a detection go to send email and log if pass the rule
        
if __name__ == "__main__":
  main()

