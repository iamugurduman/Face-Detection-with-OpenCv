import cv2
import numpy as np

vid=cv2.VideoCapture(0)

yuz_algila=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')





while(True):
    ret,frame=vid.read()
    
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#renkli resmi,tek kanala çevirerek daha verimli çalışmasını sağlıyoruz,bu olmasa da yine program çalışır ancak tavsiye edilmez.
    
    yuzler=yuz_algila.detectMultiScale(gray,1.5,5)
    for (x,y,w,h)in yuzler:
        cv2.rectangle(frame,(x,y),(x+ w, y+ h),(90,255,12),3)



    print(yuzler)
    

    cv2.imshow("Camera",frame)
    if cv2.waitKey(10)&0xFF==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()