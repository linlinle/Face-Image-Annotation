import time
import database_management as dm
from face_search import face_search
from Api_detection import face_detection
import os

group_id = 'images_96_112'
Data_path = '/Users/androiduser/Desktop/Data/Manual-Label/test_images'
images_list= os.listdir(Data_path)
if '.DS_Store' in images_list:
    images_list.remove('.DS_Store')

def find_max_dict(dict_list):
    max_dict = dict_list[0]
    for match_dict in dict_list:
        if match_dict['score'] > max_dict['score']:
            max_dict = match_dict
    return max_dict



for image_name in images_list:
    time.sleep(1)

    file_path = os.path.join(Data_path, image_name)
    match_list = face_search(file_path,group_id)

    max_dict = find_max_dict(match_list)
    if max_dict['score'] >= 40:
        dm.add_face(file_path,group_id, max_dict['user_id'], max_dict['user_info'])
    else:
        result = face_detection(file_path)
        if result['error_code'] == 18:
            result = face_detection(file_path)
        face_list = result['result']['face_list'][0]
        user_info = ' '.join(
            [str(face_list['age']), str(face_list['beauty']), face_list['expression']['type'], face_list['gender']['type']])

        dm.add_face(file_path,group_id, face_list['face_token'], user_info)


