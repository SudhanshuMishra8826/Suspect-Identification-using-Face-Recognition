import requests
import cv2
import time
from PIL import Image
#imageName = "sudhanshu_test.jpg"
#img = open(imageName,'rb')

g_url = 'http://127.0.0.1:5000'

cap = cv2.VideoCapture('http://190.10.7.91:8080/video')
i=0
while(cap.isOpened()):
    i=i+1
    ret, im= cap.read()
    v='Image'+str(i)+'.jpg'
    cv2.imwrite(v, im)
    img = open(v,'rb')
    r = requests.post("{}/{}".format(g_url,'face_search'), files={'img1':img})
    if r.ok:
        result = r.json()
        print(result)
        if result['label'] == 1:
            #cv2.imshow('Image',im)
            print("success")
        else:
            print(r.status_code)
    
