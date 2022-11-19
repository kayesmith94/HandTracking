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

# The text that you want to convert to audio
mytext = 'I love you siren!'
  
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang='en', slow=False)
  
# Saving the converted audio in a mp3 file named 
myobj.save("ily.mp3")
  

os.system("ily.mp3")
  
# Close the window 
#cap.release() 