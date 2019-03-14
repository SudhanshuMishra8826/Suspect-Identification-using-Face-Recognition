import face_recognition
import numpy as np
import pickle
import cv2
import json
from datetime import datetime
class FaceSearch:
    def __init__(self):
        print("Api Initialized")
    def searchFace(self,img,ip):
        try:
            with open ('image_encoding_file', 'rb') as fp:
                itemlist = pickle.load(fp)
            fp.close()

            with open ('celeb_name_file', 'rb') as fp:
                celebs= pickle.load(fp)
            fp.close()
            with open ('id_file', 'rb') as fp:
                idlist= pickle.load(fp)
            fp.close()
            result=[]
            image_to_test = face_recognition.load_image_file(img)
        
            image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]
            face_locations = face_recognition.face_locations(image_to_test)
            face_distances = face_recognition.face_distance(itemlist, image_to_test_encoding)

            for i, face_distance in enumerate(face_distances):
                if(face_distance<0.5):
                    result.append({"person":celebs[i],"C-ID":idlist[i]})
            if(len(result) > 0):
                with open('Result_file', 'wb') as fp:
                    pickle.dump(json.dumps({'label':1,'result':result,'bb':face_locations,'ip': ip,'date-time':str(datetime.now())}), fp)
                fp.close()
                with open("history.txt", "a") as myfile:
                    myfile.write(json.dumps({'label':1,'result':result,'bb':face_locations,'ip': ip,'date-time':str(datetime.now())}))
                    myfile.write('\n')


                return json.dumps({'label':1,'result':result,'bb':face_locations})
            else:
                return json.dumps({'label':0,'result':[]})
        except Exception as e:
            print(e)
            return json.dumps({'label':0,'result':[]})


if  __name__ =='__main__':
    srchr=FaceSearch()
    res=srchr.searchFace("sudhanshu_test.py")
    print(res)

