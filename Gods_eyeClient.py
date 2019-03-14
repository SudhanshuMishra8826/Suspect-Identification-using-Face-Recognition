import requests
import cv2

imageName = "sudhanshu_test.jpg"
img = open(imageName,'rb')

g_url = 'http://127.0.0.1:5000'


r = requests.post("{}/{}".format(g_url,'face_search'), files={'img1':img})

if r.ok:
    result = r.json()
    print(result)
    print(type(img))
    if result['label'] == 1:
        image = cv2.imread(imageName)
        cv2.imshow('Image',image)
        cv2.waitKey(0)

else:
    print(r.status_code)
