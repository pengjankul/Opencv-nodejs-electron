import numpy as np
import cv2
import time
import smtplib
import os
import sys
##from matplotlib import pyplot as plt
##from email.mime.multipart import MIMEMultipart
##from email.mime.text import MIMEText
##from email.mime.image import MIMEImage
##from email.mime.base import MIMEBase
##from email import encoders

##def sendmail():
##    server = smtplib.SMTP('smtp.gmail.com', 587)
##    server.ehlo()
##    server.starttls()
##    server.ehlo()
##    server.login("ppholmek@gmail.com", 1529900668875 )
##
##    fromaddr = "ppholmek@gmail.com"
##    toaddr = "ppholmek2@gmail.com"
##    msg = MIMEMultipart()
##    msg['From'] = fromaddr
##    msg['To'] = toaddr
##    msg['Subject'] = "facedetect"
##
##    attachment = "test.jpg"
##    fp = open(attachment, 'rb')
##    img = MIMEImage(fp.read())
##    fp.close()
##    img.add_header('Content-ID','<image1>')
##    img.add_header('Content-Disposition', 'inline', filename=attachment)
##    msg.attach(img)
##
##    server.sendmail("ppholmek@gmail.com", "ppholmek2@gmail.com", msg.as_string())
##    server.quit()
##
##    return 0

def RMBG(original_image):
    
##    original_image = cv2.imread('test.jpg')
    height, width = original_image.shape[:2]
    mask = np.zeros(original_image.shape[:2],np.uint8)    #Create a mask holder
    bgdModel = np.zeros((1,65),np.float64)  #Grab Cut the object
    fgdModel = np.zeros((1,65),np.float64)

    #Hard Coding  Rect The object must lie within this rect.
##    rect = (800,0,410,700) #1 human right
##    rect = (20,25,450,680) #1 human left
    rect = (400,20,800,680) #1 human center

    cv2.grabCut(original_image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img1 = original_image*mask[:,:,np.newaxis]
##    cv2.imwrite('testcut.png',img1)
    
    tmp = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #transparent image
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(img1)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    cv2.imwrite("img_transparent.png", dst)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
count = 5
face_count = sys.argv[1]
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
##    cv2.putText(img,'Found face = {0}'.format(len(faces)),
##                    (420,450), font, 0.8, (255,0,0),2, cv2.LINE_AA)
    img = cv2.resize(img, (1280, 720), interpolation=cv2.INTER_CUBIC)
####    cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
##    cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN,
##                              cv2.WINDOW_FULLSCREEN)
    cv2.imshow('img', img)
    
    if len(faces) >= int(face_count): #10people
        if count != 0:
            cv2.putText(img,'{0}'.format(str(count)),
                (250,300), font, 10, (0,255,0),2)
            count -= 1
            time.sleep(1)
            cv2.imshow('img',img)
        else:
            cv2.imwrite('test.jpg',img)
            time.sleep(1)
            
            original_image = cv2.imread('test.jpg')
            RMBG(original_image)
         
##            img1 = cv2.imread('3.jpg')
##            merge(img1)
            
            #sendmail()
            count = 5
            
    else:
        count = 5

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print ('close')
        sys.stdout.flush()
        break
    
cap.release()
cv2.destroyAllWindows()


