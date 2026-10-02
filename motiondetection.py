import cv2                                         # importing the opencv library
import threading                                   # importing the threading module to handle multiple frames simultaneously
import imutils                                     # a library to handle images and video in python 
import winsound                                    # for playing sound
import datetime    
import smtplib
import os        
import imghdr                                      # To check image file type
from email.message import EmailMessage             # To send emails


sender_mail = "your mail"
sender_password = "your password"
receiver_mail = "Enter receiver's mail"             #  Enter Receivers Mail id 
smtp_server = 'smtp.gmail.com'                      #  Gmail SMTP server
smtp_port = 587                                     #  Port used by Google for 


camera= cv2.VideoCapture(0, cv2.CAP_DSHOW)               # creating  an object of VideoCapture.and

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 850)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 650)

sk, start_frame= camera.read()                        # capturing the first motion or compairee the frames
start_frame=imutils.resize(start_frame, width=500)
start_frame=cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame=cv2.GaussianBlur(start_frame,(21,21),0)

alarm= False
alarm_mode=False
alarm_counter=(0)

def beeping(): 
    global alarm                               # function to play alarm sound when there is a movement
    for sk in range(50):
        if not alarm_mode:
            break
        print("alarm")
        winsound.Beep(2500,3000)              # the frequency and duration of the beep
    alarm=False

while True:
   _, frame = camera.read()                                                    # reading a new frame from the video stream
   frame= imutils.resize(frame, width=500)
   
   if alarm_mode:                                                               # if the alram mode is on then keep updating
        frame_black_white=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_black_white=cv2.GaussianBlur(frame_black_white,(5,5),0)

        difference = cv2.absdiff(frame_black_white, start_frame)                # calculate the absolute difference between two consecutive frames
        threshold =cv2.threshold(difference, 25,255, cv2.THRESH_BINARY)[1]
        start_frame=frame_black_white

        if threshold.sum()> 3000:
            alarm_counter +=1
        else:
            if alarm_counter>0:
                alarm_counter -=1

        cv2.imshow ("camera", threshold)
   else:
        cv2.imshow("camera", frame)

   if alarm_counter> 20:    # 
        if not alarm:
            alarm=True
            threading.Thread(target=beeping).start()        
   key = cv2.waitKey(30)                       # waits 30 milliseconds for a keyboard break the alarm  loop
   if key == ord('t'):
        alarm_mode= not alarm_mode
        alarm_counter=0
   if key == ord("q"):
        alarm_mode=False 
        break

################################################/* Email sent code start form here */########################################################
if alarm_counter:
    timestamp= datetime.datetime.now().strftime("%Y-%M-%d_%H-%M-%S")
    image_path= f"Real_time_motion_image.jpg"
    cv2.imwrite(image_path,frame)
    
    # sending an email with the picture of the event
    msg = EmailMessage()
    msg['Subject'] = f'Motion is detected at {timestamp}'
    msg['From'] = sender_mail
    msg['To'] = receiver_mail
    
#  Attach file or image
with  open(image_path,'rb') as attachment:
    image_data = attachment.read()
    image_type = imghdr.what(attachment.name)
    msg.add_attachment(image_data, maintype= "image", ubtype=image_type, filename=attachment.name)

# # # Send the message via our own SMTP server.
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_mail,sender_password)
    server.send_message(msg) 

# Release everything if job is finished
os.remove(image_path)

camera.release()  
cv2.destroyAllWindows()
