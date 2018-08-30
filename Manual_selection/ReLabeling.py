import cv2
import os
import pandas as pd
import numpy as np

from Manual_selection.utils import is_right_age,check_label

MAX_age = 100
MIN_age = 1



Data_path = '/Users/androiduser/Desktop/Data/Manual-Label'
kiwi = pd.read_csv(os.path.join(Data_path,'Kiwi.txt'), sep='\s',index_col=False, names=['filen_ame','gender','age1','age2','mood'])
os.chdir(os.path.join(Data_path + '/images'))
for index,name in enumerate(kiwi['filen_ame']):
    img = cv2.imread(name, cv2.IMREAD_COLOR)
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, img)
    cv2.waitKey(10)
    gender = kiwi.loc[index,['gender']].values[0]
    age1 = kiwi.loc[index,['age1']].values[0].strip('(,')
    age2 = kiwi.loc[index,['age2']].values[0].strip(')')
    mood = kiwi.loc[index,['mood']].values[0]
    print('file: {} ,gender: {}, age: {} ~ {}, mood: {}'.format(name, gender, age1, age2, mood))
    new_age = input('nwe age: ')
    right_age =  is_right_age(int(new_age), MIN_age, MAX_age)
    kiwi.loc[index,['age1']] = str(right_age)
    print(kiwi.loc[index,['age1']].values[0].strip('(,'))


#####################################Ingore#############################################
images_list= os.listdir(os.getcwd())
re_image_list = np.array(kiwi['filen_ame']).tolist()

retD = list(set(images_list).difference(set(re_image_list)))

for name in images_list:
    img = cv2.imread(name, cv2.IMREAD_COLOR)
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, img)
    cv2.waitKey(10)
    while True:
        input_str = input(name+'*****的3个标签属性(性别 年龄 心情)：')
        input_list = input_str.split(sep=' ')
        if check_label(input_list):
            break
    gender, age, mood= input_list
    row = pd.Series([name, gender, age, mood],index=['file_name','gender','age','mood'])
    kiwi = kiwi.append(row,ignore_index=True)


os.chdir(os.path.dirname(os.getcwd()))
#os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)))

kiwi.to_csv(os.path.join(Data_path,'kiwi_Asia.txt'),sep=' ',columns=['filen_ame','gender','age1','mood'], header=False, index=False)
