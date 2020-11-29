import os
import smtplib
import imghdr
import cv2
import numpy as np
import time
import darknet

from email.message import EmailMessage
from email.mime.text import MIMEText
from setEmail import email
from fpdf import FPDF
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

EMAIL_USER = "knockknockcis3296@gmail.com"
EMAIL_PASSWORD = "Cis3296!"

msg = EmailMessage()
msg['Subject'] = 'Delivery detected'
msg['From'] = EMAIL_USER
with open('userEmail.txt','r') as userEmail:
	emailAddress = userEmail.read()
msg['To'] = emailAddress
msg.set_content('A delivery at your door was detected at ' + current_time+ '. Please check attached text file for more information!')

#Section to convert a text file to a pdf
#======================================================================#
def txtToPDF(filePath):

	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 10)

	f = open(filePath, "r")
	for i in f:
		pdf.cell(0,txt = i, ln = 2)

	return pdf.output("output.pdf")

#=======================================================================#

#Section to prepare sending an email
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

#Attaches the pdf to the email
def attachPDF(filePath):
	with open(filePath,'rb') as f:
		file_data = f.read()
		file_name = f.name
	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)

def sendPDF(filePath):
	attachPDF(filePath)

#Method to send email with attachments as parameters
def sendAttachments(imgPath, pdfPath):
	sendIMG(imgPath)
	sendPDF(pdfPath)

txtFile= "/Users/harith.siddiqui754/PycharmProjects/kkEmail/sampleFile.txt"
#txtToPDF(txtFile)

sendAttachments('test.jpg', txtFile)
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

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_USER, EMAIL_PASSWORD)
	smtp.send_message(msg)
#=======================================================================#


############################
#write detections to log file
############################
def logging(label, confidence):
    file = "detection_logs/"
    file += datetime.today().strftime('%Y-%m-%d')
    f = open(file, "a")
    output = datetime.now().strftime('%H:%M') + "\n"
    if confidence >= 90:
        output += "\tDelivery driver detected!\n"
    else:
        output += "\tDelivery driver may have been detected!\n"
    output += "\t\t{}: {}% confident".format(label, confidence) + "\n"
    f.write(output)
    f.close




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
     if not os.path.exists(configPath):
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    if netMain is None:
        netMain = darknet.load_net_custom(configPath.encode(
            "ascii"), weightPath.encode("ascii"), 0, 1)  # batch size = 1
    if metaMain is None:
        metaMain = darknet.load_meta(metaPath.encode("ascii"))
    if altNames is None:
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents,
                                  re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass
    #decide input source
    cap = cv2.VideoCapture("")#<-enter input video address here
    
    #Uncomment below to get video from camera
    #RTSP_URL = #enter RTSP URL here if using a camear
    #cap = cv2.VedeoCapture(RTSP_URL)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    new_height, new_width = frame_height // 2, frame_width // 2
    #set output video footage
     out = cv2.VideoWriter("./output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 10.0,(new_width, new_height))
    #a reuse image for each detection
    darknet_image = darknet.make_image(new_width, new_height, 3)
    #loop through the video
    while True:
    	prev_time = time.time()
    	ret, frame_read = cap.read()
    	# if no more frame can be read, end loop
    	if not ret:
        	break
        frame_rgb = cv2.cvtColor(frame_read, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb,
                                   (new_width, new_height),
                                   interpolation=cv2.INTER_LINEAR)

        darknet.copy_image_from_bytes(darknet_image,frame_resized.tobytes())
	detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.25)
        #a detection go through the rule
	 for label, confidence, bbox in detections:
		confidence = str(round(confidence * 100, 2))
	    	if confidence > 80:
	    		logging(label, confidence)
        #a detection go to send email and log if pass the rule
if __name__ == "__main__":
  main()

