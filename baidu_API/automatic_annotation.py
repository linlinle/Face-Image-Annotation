import time
import os
import pandas as pd
from baidu_API.Api_detection import face_detection




Data_path = '/Users/androiduser/Desktop/Data/Manual-Label/images'
images_list= os.listdir(Data_path)
kiwi = pd.DataFrame(columns=['file_name','age','beauty','expression','gender'])
if '.DS_Store' in images_list:
    images_list.remove('.DS_Store')
os.chdir(Data_path)

for name in images_list:
    file_path = os.path.join(Data_path, name)
    result = face_detection(file_path)
    if result['error_code'] == 18:
        time.sleep(1)
        result = face_detection(file_path)
    print(name, result)

    if result['error_code'] == 0:
        face_list = result['result']['face_list'][0]
        re_name = face_list['face_token'] + '.jpg'
        os.rename(name,re_name)
        row = pd.Series([re_name, face_list['age'], face_list['beauty'], face_list['expression']['type'],face_list['gender']['type']],
                        index=['file_name','age','beauty','expression','gender'])
        kiwi = kiwi.append(row, ignore_index=True)

    elif result['error_code']  == 222202:
        os.remove(file_path)



kiwi.to_csv(os.path.join(os.path.dirname(Data_path),'kiwi_asia1.txt'),sep=' ', header=True, index=False)


