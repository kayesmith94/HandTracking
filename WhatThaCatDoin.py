# OpenCV program to detect cat face in real time 
# import libraries of python OpenCV 
# where its functionality resides 
import cv2
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# load the required trained XML classifiers 
# https://github.com/Itseez/opencv/blob/master/ 
# data/haarcascades/haarcascade_frontalcatface.xml 
# Trained XML classifiers describes some features of some 
# object we want to detect a cascade function is trained 
# from a lot of positive(faces) and negative(non-faces) 
# images. 
face_cascade = cv2.CascadeClassifier('HandTracking/haarcascade_frontalcatface_extended.xml') 
  
# capture frames from a camera 
cap = cv2.VideoCapture(0) 
  
# loop runs if capturing has been initialized. 
while True: 
  
    # reads frames from a camera 
    ret, img = cap.read() 
  
    # convert to gray scale of each frames 
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
  
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(rgb, 1.3, 5) 
  
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = rgb[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w]
        os.system("ily.mp3")
  
  
    # Display an image in a window 
    cv2.imshow('img',img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window 
#cap.release() 