import numpy as np
import cv2 # pip install opencv2
import random
'''import pyttsx3

engine = pyttsx3.init()
'''
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_mouth.xml')#cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
#mouth_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_mouth.xml')

# For user message
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
weared_mask_font_color = ( 0, 255, 0)
not_weared_mask_font_color = (0, 0, 255)
thickness = 2
font_scale = 1
weared_mask = "Thank You for wearing MASK"
not_weared_mask = "Please wear MASK to defeat Corona"

# Read video
cap = cv2.VideoCapture(1)
'''
engine.say('hello guys')
engine.runAndWait()
engine.say('welcome to face detector')
engine.runAndWait()
'''
while 1:
    # Get individual frame
    ret, img = cap.read()

    # Convert Image into gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect face 
    faces = face_cascade.detectMultiScale(gray, 1.9, 10)

    # detect eye
    eye = eye_cascade.detectMultiScale(gray, 1.05, 10)

    # detect mouth
    #mouth = mouth_cascade.detectMultiScale(gray, 1.1, 4)

    if(len(faces) == 0 and len(eye) == 0):
        pass #engine.say('please come to the focus point')
    elif(len(faces) == 0 and len(eye)>0):
        #if(len(mouth) == 0):
            # engine.say(weared_mask)
            # engine.runAndWait()
        #for(x,y,w,h) in eye:
         #   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    elif(len(faces)>0):
        # engine.say(not_weared_mask)
        # engine.runAndWait()
        #for(x,y,w,h) in faces:
         #   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img, not_weared_mask, org, font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)

    # Show frame with results
    cv2.imshow('Mask Detection', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27: #27 is ascii value of 'esc' key
        break

# engine.say('Thank you for using me ')
# engine.runAndWait()

# Release video
cap.release()
cv2.destroyAllWindows()
