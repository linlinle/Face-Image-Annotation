
import os
import pandas as pd
import cv2
from utils import check_label


Data_path = '/Users/androiduser/Desktop/Data/Manual-Label'
os.chdir(os.path.join(Data_path + '/self_images'))
images_list= os.listdir(os.getcwd())
#images_list.remove('.DS_Store')
kiwi = pd.DataFrame(columns=['file_name','gender','age','mood'])
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

kiwi.to_csv(os.path.join(Data_path,'kiwi_self.txt'),sep=' ',columns=['file_name','gender','age','mood'], header=False, index=False)

