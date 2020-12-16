import cv2 
import sys
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
count =0;
cap = cv2.VideoCapture(0)
temp=1;
temp1=1;


while(1):
    ret, img = cap.read() 
    resize_img=cv2.resize(img,(640,480))
    gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.imshow('img',resize_img)
    for (x,y,w,h) in faces:
        cv2.rectangle(resize_img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = resize_img[y:y+h, x:x+w]
        temp=1;
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        cv2.imshow('img',resize_img)

        for (ex,ey,ew,eh) in eyes:
       	    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
       	    cv2.imshow('img',resize_img)
       	    print ('eye detected')
       	    count=0;
       	    temp=0;

    if (temp==1):
        count = count+1
        print (count)
        if count>100:
            print('long count')
            count=0;


    k = cv2.waitKey(30) & 0xff
    if k == 27:
       break
cap.release()

cv2.destroyAllWindows() 
