import sys
import os
import cv2
import scipy.io
import numpy as np
import mtcnn

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'preprocess'))
from detector import FaceDetector


IMG_DIR = 'images'
FILE = 'Kiwi.txt'

# GENDER_LIST =['f','m']
# AGE_LIST = ['(0, 2)','(4, 12)','(15, 32)','(38, 53)','(60, 100)']
# EMOTION_LIST = ["happy", "neutral", "sad"]

def whichgender(str):
    gender_list =['f','m']
    assert str in gender_list
    return gender_list.index(str)

def howold(str):
    age_list = ['(0, 2)','(4, 6)','(8, 12)','(15, 20)','(25, 32)','(38, 43)','(48, 53)','(60, 100)']
    assert str in age_list
    index = age_list.index(str)
    if(index==1 or index == 2):
        index = 1
    elif(index==3 or index == 4):
        index = 2
    elif(index==5 or index == 6):
        index = 3
    elif(index==7):
        index = 4
    else:
        index = 0 
    return index

def whichemotion(str):
    emotion_list = ["happy", "surprise", "neutral", "sad", "angry"]
    assert str in emotion_list
    index = emotion_list.index(str)
    if(index==0 or index == 1):
        index = 0
    elif(index==2):
        index = 1
    else:
        index = 2
    return index

def read_property(file):
    gender_list =['f','m']
    age_list = ['(0, 2)','(4, 6)','(8, 12)','(15, 20)','(25, 32)','(38, 43)','(48, 53)','(60, 100)']
    emotion_list = ["happy", "surprise", "neutral", "sad", "angry"]
    f = open(file, 'r')
    content = f.readlines()
    dic = {}
    for i in range(0, len(content)):
        line = content[i].strip().split('\t')
        if len(line)==4 and line[1] in gender_list and line[2] in age_list and line[3] in emotion_list:
            dic.update({line[0] : [whichgender(line[1]), howold(line[2]), whichemotion(line[3])]})
    print("kiwi: %d samples"%len(dic))
    return dic

def create_database(img_dir, file):
    image = []
    gender = []
    age = []
    emotion = []

    detector = FaceDetector()
    dic = read_property(file)
    
#     abs_path = os.path.join(img_dir, 'CF7AF8-96DD-480B-9A50-AC5C3787DA08.jpeg')
#     img = cv2.imread(abs_path)
#     _, points = detector.detect(img)
#     aligned = detector.align(img, landmark = points[:, 0].reshape( (2,5) ).T, image_size = [112, 112])
#     resized = cv2.resize(aligned, (64,64))
    num = 0
    for key , value in dic.items():
        num+=1
        print(str(num))
        print(key)
        
        abs_path = os.path.join(img_dir, key)
        if not os.path.exists(abs_path):
            continue
        img = cv2.imread(abs_path)
        _, points = detector.detect(img)
        
        if len(points) != 0:
            if len(points[0]) !=0:
                aligned = detector.align(img, landmark = points[:, 0].reshape( (2,5) ).T, image_size = [112, 112])
                resized = cv2.resize(aligned, (64,64))
                 
                image.append(resized)
                gender.append(value[0])
                age.append(value[1])
                emotion.append(value[2])
         
    mat = { 'image':np.array(image),
            'gender':np.array(gender),
            'age':np.array(age),
            'emotion':np.array(emotion),
            'db':"kiwi_db",
            'img_size':64,
            'min_score':1 }
    scipy.io.savemat("kiwi_db.mat", mat)
    
create_database(IMG_DIR, FILE)