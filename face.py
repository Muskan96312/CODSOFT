#pip install opencv-python

import cv2
video_cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' )
while True:
    ret,frame=video_cap.read()
    if not ret:
        break
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF==ord('g'):
        break
        gray_frame=cv2.equalizeHist(gray_frame) 
        
    faces=face_cascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Face Detection',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video_cap.release()
cv2.destroyAllWindows() 



