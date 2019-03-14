from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import hashlib
import base64
import pickle
import ast
import io
import requests
import json
import time
import json
from PIL import Image

from face_search import FaceSearch

app = Flask(__name__)

@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/', methods=['GET'])
def home():
    return jsonify({'Message': 'API Working!!'})

@app.route('/face_search',methods=['POST'])
def face_search():
    ip= request.remote_addr
    img1 = request.files['img1']
    t = time.time()
    result = srch.searchFace(img1,ip)
    print(time.time() - t)
    return result

@app.route('/report')
def rep():
    with open ('result_file', 'rb') as fp:
        itemlist = pickle.load(fp)
    fp.close()
    return(jsonify(ast.literal_eval(itemlist)))

@app.route('/data',methods=['GET'])
def dat():
    with open ('result_file', 'rb') as fp:
        itemlist = pickle.load(fp)
    fp.close()
    # print(itemlist)
    # js=jsonify(itemlist)
    # js=js.json()
    js = json.loads(itemlist)
    name=js['result'][0]["person"]
    Cid=js['result'][0]["C-ID"]
    date=js['date-time']
    ip=js['ip']
    return render_template('index.html',name=name,date=date,ip=ip,Cid=Cid)

@app.route('/history')
def history():
    itemlis=''
    with open ('history.txt', 'r') as fp:
        for f in fp:
            itemlis=itemlis+f+'\n'
    fp.close()
    return(itemlis)

if __name__=='__main__':
    srch = FaceSearch()
    app.run(debug=True)
