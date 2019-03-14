import requests
import cv2
import time
import hashlib
import base64
from PIL import Image
import numpy
#imageName = "sudhanshu_test.jpg"
#img = open(imageName,'rb')

g_url = 'http://127.0.0.1:5000'

cap = cv2.VideoCapture('http://190.10.7.91:8080/video')
i=0
while(cap.isOpened()):
    i=i+1
    ret, im= cap.read()
    result, img= cv2.imencode('.jpg', im)
    img = img.tostring()
    img = base64.b64encode(img)
    img = img.decode('utf-8')
    r = requests.post("{}/{}".format(g_url,'face_search'), data={'img1':img})
    if r.ok:
        result = r.json()
        print(result)
        if result['label'] == 1:
            #cv2.imshow('Image',im)
            print("successful") 
        else:
            print(r.status_code)
