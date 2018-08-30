import time
import database_management as dm
from face_search import face_search
from Api_detection import face_detection
import os, shutil

def mkdirs(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


def get_structure_list(dir_path):
    structure = []
    folder_list = os.listdir(dir_path)
    if '.DS_Store' in folder_list:
        folder_list.remove('.DS_Store')
    for folder in folder_list:
        structure.append(os.listdir(os.path.join(dir_path,folder)))


    # with open('structure.json','a') as fj:
    #     json.dump(structure,fj)

    return structure

def main(group_id,root_path,makedir_path):

    images_list= os.listdir(root_path)
    user_excited = get_structure_list(makedir_path)

    #local_group = dict()

    if '.DS_Store' in images_list:
        images_list.remove('.DS_Store')


    for image_name in images_list:
        face_token = image_name.split('.')[0]
        face_id = face_token.replace('-','')
        file_path = os.path.join(root_path, image_name)
        max_dict = face_search(file_path,group_id)
        if max_dict['error_code'] == 222202:
            print("照片中没有人脸")
            continue
        if max_dict['error_code'] == 18:
            print("QPS过载")
            time.sleep(0.5)
            max_dict = face_search(file_path, group_id)

        max_dict = max_dict['result']['user_list'][0]

        if image_name in user_excited or max_dict['score'] == 100:
            print(image_name + "  已经存在")
            continue

        if max_dict['score'] >= 80:# 匹配成功

            shutil.copy(file_path, os.path.join(makedir_path,max_dict['user_id']))
            print(image_name + '=======>'+ max_dict['user_id'])

        else:                                                           # 新的face
            dm.add_face(file_path,group_id, face_id, " one person")

            mkdirs(os.path.join(makedir_path,face_id))
            shutil.copy(file_path, os.path.join(makedir_path,face_id))
            print("新建user_id : "+ face_id )

        user_excited.append(face_id)



if __name__ == "__main__":
    main(group_id = 'paqu',
    root_path = '/Users/androiduser/Desktop/Data/Manual-Label/paqu_images',
    makedir_path = '/Users/androiduser/Desktop/Data/Manual-Label/paqu_test'
    )