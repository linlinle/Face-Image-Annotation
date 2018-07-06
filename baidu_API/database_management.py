# encoding:utf-8
import base64
import urllib3
from http_request import http_request
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)




def add_face(file_path,group_id,user_id,user_info):
     '''
     人脸注册:用于向人脸库中新增用户，及组内用户的人脸图片，

     '''
     with open(file_path, 'rb') as f:
         img = base64.b64encode(f.read())

     request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
     params = {'image': '' + str(img, 'utf-8') + '', 'image_type': 'BASE64', "group_id": group_id, "user_id": user_id, 'user_info':user_info}

     result = http_request(params, request_url)
     print(result)

def update_face(file_path,group_id,user_id,user_info):
    '''
    人脸更新:针对一个user_id执行更新操作，新上传的人脸图像将覆盖此user_id原有所有图像。
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/update"
    with open(file_path, 'rb') as f:
        img = base64.b64encode(f.read())

    params = {'image': '' + str(img, 'utf-8') + '', 'image_type': 'BASE64', "group_id": group_id, "user_id": user_id,
              'user_info': user_info}
    result = http_request(params, request_url)

    print( result)

def delete_face(group_id,user_id,face_token):
    '''
    删除人脸 ： 删除用户的某一张人脸，如果该用户只有一张人脸图片，则同时删除用户。

    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/delete"
    params = {"group_id": group_id, "user_id": user_id, 'face_token': face_token}
    result = http_request(params, request_url)

    print( result)

def get_user_info(group_id,user_id):
    '''
    用户信息查询：获取人脸库中某个用户的信息(user_info信息和用户所属的组)。
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/get"
    params = {"group_id": group_id, "user_id": user_id,}
    result = http_request(params, request_url)

    print( result)

def get_face_list(group_id,user_id):
    '''
    获取用户人脸列表
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist"

    params = {"group_id": group_id, "user_id": user_id,}
    result = http_request(params, request_url)

    print( result)

def get_users_list(group_id):

    '''
    获取用户人脸列表:用于查询指定用户组中的用户列表。

    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers"
    params = {"group_id": group_id}

    result = http_request(params, request_url)

    print( result)

def delete_user(group_id,user_id):
    '''
    删除用户：用于将用户从某个组中删除。

    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/delete"

    params = {"group_id": group_id, "user_id": user_id,}
    result = http_request(params, request_url)

    print( result)


def add_group(group_id):

    '''
    创建用户组 : 用于创建一个空的用户组，如果用户组已存在 则返回错误。

    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/add"
    params = {"group_id":group_id}
    result = http_request(params, request_url)

    print( result)

def delete_group(group_id):
    '''
    删除用户组：删除用户组下所有的用户及人脸，如果组不存在 则返回错误。
。

    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/delete"

    params = {"group_id": group_id}
    result = http_request(params, request_url)

    print( result)

def get_group_list():
    '''
    组列表查询 : 用于查询用户组的列表。

    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getlist"


    params = {"start": 0, 'length':100}
    result = http_request(params, request_url)

    print( result)


if __name__ == "__main__":
    #get_users_list('images_96_112')
    #add_group("images_96_112")
    add_face('/Users/androiduser/Desktop/Data/Manual-Label/images_96_112/0a21f833246d4add398c2b296ffd3a27.jpg','images_96_112','0a21f833246d4add398c2b296ffd3a27','22 40.43471909 none male')
    #update_face('/Users/androiduser/Desktop/Data/Manual-Label/images_96_112/0a74a73c44dcd7e98db9197565a664a8.jpg','images_96_112','0a1c5022f524ba88a902c2cfe93bb282','21 50.43471909 none fmale')
    #delete_face('images_96_112','0a1c5022f524ba88a902c2cfe93bb282','0a74a73c44dcd7e98db9197565a664a8')
    #delete_user('images_96_112','0a1c5022f524ba88a902c2cfe93bb282')
    #delete_group('0_14mca1157')
    #get_group_list()