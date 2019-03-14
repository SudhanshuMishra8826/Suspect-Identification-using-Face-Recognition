import face_recognition
import numpy as np
import pickle

known_sudhanshu_image = face_recognition.load_image_file("sudhanshu.jpg")
known_deepak_image = face_recognition.load_image_file("deepak.jpg")
known_harsh_image = face_recognition.load_image_file("harsh.jpg")


sudhanshu_face_encoding = face_recognition.face_encodings(known_sudhanshu_image)[0]
deepak_face_encoding = face_recognition.face_encodings(known_deepak_image)[0]
harsh_face_encoding = face_recognition.face_encodings(known_harsh_image)[0]





known_encodings = [
    sudhanshu_face_encoding,
    deepak_face_encoding,
    harsh_face_encoding, 
]


celeb_names=["Sudhanshu Mishra", "Deepak Yadav","Harsh Bidhuri"]
id=['137','245','267']

with open('image_encoding_file', 'wb') as fp:
    pickle.dump(known_encodings, fp)
fp.close()
with open ('image_encoding_file', 'rb') as fp:
    itemlist = pickle.load(fp)
print(itemlist)
fp.close()
with open('celeb_name_file', 'wb') as fp:
    pickle.dump(celeb_names, fp)
fp.close()
with open ('celeb_name_file', 'rb') as fp:
    itelist = pickle.load(fp)
print(itelist)
fp.close()


with open('id_file', 'wb') as fp:
    pickle.dump(id, fp)
fp.close()
with open ('id_file', 'rb') as fp:
    itelist = pickle.load(fp)
print(itelist)
fp.close()
'''f= open("celebencodings.txt","w+")
f.write(''.join(str(e) for e in known_encodings))
f.close()
f= open("celebencodings.txt","r")
ft=f.read()
ftlist=[int(i) for i in ft]
print(ftlist)
f.close'''
