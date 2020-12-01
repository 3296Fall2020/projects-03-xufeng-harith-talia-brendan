import os
import smtplib
import imghdr
import cv2
import numpy as np
import time
import darknet
import sys
from email.message import EmailMessage
from email.mime.text import MIMEText
from fpdf import FPDF
from datetime import datetime
# Early exit
if len(sys.argv)<2:
	printf("Enter a video input path!")
	exit()
videoInput=sys.argv[1]
#determine time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#email initialization
EMAIL_USER = "knockknockcis3296@gmail.com"
EMAIL_PASSWORD = "Cis3296!"
msg = EmailMessage()
msg['Subject'] = 'Delivery detected'
msg['From'] = EMAIL_USER
with open('userEmail.txt','r') as userEmail:
	emailAddress = userEmail.read()
msg['To'] = emailAddress


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
def sendIMG(filePath):
  attachImage(filePath)

def attachImage(filePath):
  with open(filePath,'rb') as f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    file_name=f.name
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

def sendPDF(filePath):
  attachPDF(filePath)

def attachPDF(filePath):
  with open(filePath,'rb') as f:
    file_data=f.read()
    file_name=f.name
    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

#Method to send email with attachments as parameters
def sendAttachments(imgPath, pdfPath,label,confidence):
  if confidence>float(89.9):
    msg.set_content('A '+label+' was detected at ' + current_time+ '. Please check attached text file for more information!')
  else:
    msg.set_content('Looks like a '+label+' stopped by your door at ' + current_time+ '. Please check attached text file for more information!')
  sendIMG(imgPath)
  sendPDF(pdfPath)
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	  smtp.login(EMAIL_USER, EMAIL_PASSWORD)
	  smtp.send_message(msg)

#sendAttachments('test.jpg', txtFile)
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

#=======================================================================#

############################
#write detections to log file
############################
def logging(label, confidence, imgPath):
    file = "detection_logs/"
    file += datetime.today().strftime('%Y-%m-%d')
    txtFile = file
    f = open(file, "a")
    output = datetime.now().strftime('%H:%M') + "\n"
    if confidence >= float(90):
        output += "\tDelivery driver detected!\n"
    else:
        output += "\tDelivery driver may have been detected!\n"
    output += "\t\t{}: {}% confident".format(label, confidence) + "\n"
    f.write(output)
    f.close
    sendAttachments(imgPath, file,label,confidence)




#################################################
# Drawing box on img according to the detection 
#################################################
def convertBack(x, y, w, h):
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax


def cvDrawBoxes(detections, img):
    # Colored labels dictionary
    color_dict = {
        'amazonCourier' : [0, 255, 255], 'fedexCourier': [238, 123, 158], 'ups_courier' : [24, 245, 217], 'uspsCourier' : [224, 119, 227]
    }
    
    for detection in detections:
        # print("detections[0]: " + str(detection[0]))
        # print("detections[1]: " + str(detection[1]))
        x, y, w, h = detection[2][0],\
            detection[2][1],\
            detection[2][2],\
            detection[2][3]
        name_tag = str(detection[0])#.decode())
        for name_key, color_val in color_dict.items():
            if name_key == name_tag:
                color = color_val 
                xmin, ymin, xmax, ymax = convertBack(
                float(x), float(y), float(w), float(h))
                pt1 = (xmin, ymin)
                pt2 = (xmax, ymax)
                cv2.rectangle(img, pt1, pt2, color, 1)
                cv2.putText(img,
                            detection[0] +
                            " [" + str(detection[1]) + "]",
                            (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            color, 2)
    return img



##################################
#The main part
##################################
def main():  
    # YOLO and darknetconfiguration
    configPath = "./cfg/knockknock_cfg.cfg"                                 # Path to cfg
    weightPath = "./knockknock_cfg_best.weights"                                 # Path to weights
    metaPath = "./data/obj.data"                                    # Path to meta data
    if not os.path.exists(configPath):                              # Checks whether file exists otherwise return ValueError
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    network, class_names, class_colors = darknet.load_network(
            configPath,
            metaPath,
            weightPath,
            batch_size=1
        )
   
    
    #cap = cv2.VideoCapture(0)                                      # Uncomment to use Webcam
    cap = cv2.VideoCapture(videoInput)                             # Local Stored video detection - Set input video
    frame_width = int(cap.get(3))                                   # Returns the width and height of capture video
    frame_height = int(cap.get(4))
    # Set out for video writer
    fileName = datetime.now().strftime("%B-%d-%y_%H:%M:%S")
    outputPath="./results/"+fileName+".avi"
    out = cv2.VideoWriter(                                          # Set the Output path for video writer
        outputPath, cv2.VideoWriter_fourcc(*"MJPG"), 10.0,
        (frame_width, frame_height))

    print("Analyze starts..")

    darknet_image = darknet.make_image(frame_width, frame_height, 3) # Create image according darknet for compatibility of network
    x=float(0)
    while True:                                                      # Load the input frame and write output frame.
        prev_time = time.time()
        # print("line 107 pass")
        ret, frame_read = cap.read()                                 # Capture frame and return true if frame present
        # print("line 109 pass")
        # For Assertion Failed Error in OpenCV
        if not ret:                                                  # Check if frame present otherwise he break the while loop
            break

        frame_rgb = cv2.cvtColor(frame_read, cv2.COLOR_BGR2RGB)      # Convert frame into RGB from BGR and resize accordingly
        #print("line 116 pass")
        frame_resized = cv2.resize(frame_rgb,
                                   (frame_width, frame_height),
                                   interpolation=cv2.INTER_LINEAR)
        #print("line 117 pass")
        darknet.copy_image_from_bytes(darknet_image,frame_resized.tobytes())                # Copy that frame bytes to darknet_image
        #print("line 121 pass")
        # detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.5)    # Detection occurs at this line and return detections, for customize we can change the threshold.                                                                                   
        detections = darknet.detect_image(network, class_names, darknet_image, thresh=0.8)
        #print("line 124 pass")
        image = cvDrawBoxes(detections, frame_resized)               # Call the function cvDrawBoxes() for colored bounding box per class
        #print("line 126 pass")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


        if detections:
          if float(detections[0][1])>x:
            snap=image
            detection=detections
            x=float(detections[0][1])
           
        # print(1/(time.time()-prev_time))
        #cv2.imshow('Demo', image)                                    # Display Image window
        cv2.waitKey(3)
        out.write(image)                                             # Write that frame into output video
    # print("detections[0]: " + str(detections[0][0]))
    cap.release()                                                    # For releasing cap and out. 
    out.release()
    if x>float(80):
      snapPath="./results/"+fileName+".jpg"
      cv2.imwrite(snapPath,snap)
      label=str(detection[0][0])
      confidence=float(detection[0][1])
      logging(label,confidence,snapPath)
    
    print("Analyze Completed")
if __name__ == "__main__":
  main()

