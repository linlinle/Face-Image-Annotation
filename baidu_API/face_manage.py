# encoding:utf-8
import base64
from util import url_request,access_token

header = ['Content-Type', 'application/json']


def add_face(file_path,group_id,user_id,user_info):
     '''
     人脸注册:用于向人脸库中新增用户，及组内用户的人脸图片，

     '''
     with open(file_path, 'rb') as f:
         img = base64.b64encode(f.read())

     url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add" + "?access_token=" + access_token

     params = {'image': '' + str(img, 'utf-8') + '', 'image_type': 'BASE64', "group_id": group_id, "user_id": user_id, 'user_info':user_info}

     result = url_request(url,header,params)
     print(result)

def update_face(file_path,group_id,user_id,user_info):
    '''
    人脸更新:针对一个user_id执行更新操作，新上传的人脸图像将覆盖此user_id原有所有图像。
    '''
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/update" + "?access_token=" + access_token

    with open(file_path, 'rb') as f:
        img = base64.b64encode(f.read())

    params = {'image': '' + str(img, 'utf-8') + '', 'image_type': 'BASE64', "group_id": group_id, "user_id": user_id,
              'user_info': user_info}

    result = url_request(url, header, params)

    print( result)

def delete_face(group_id,user_id,face_token):
    '''
    删除人脸 ： 删除用户的某一张人脸，如果该用户只有一张人脸图片，则同时删除用户。

    '''

    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/delete" + "?access_token=" + access_token

    params = {"group_id": group_id, "user_id": user_id, 'face_token': face_token}
    result = url_request(url, header, params)

    print( result)

def get_user_info(group_id,user_id):
    '''
    用户信息查询：获取人脸库中某个用户的信息(user_info信息和用户所属的组)。
    '''
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/get" + "?access_token=" + access_token

    params = {"group_id": group_id, "user_id": user_id,}
    result = url_request(url, header, params)

    print( result)

def get_face_list(group_id,user_id):
    '''
    获取用户人脸列表
    '''

    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist" + "?access_token=" + access_token


    params = {"group_id": group_id, "user_id": user_id,}
    result = url_request(url, header, params)

    print( result)

def get_users_list(group_id):

    '''
    获取用户人脸列表:用于查询指定用户组中的用户列表。

    '''
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers" + "?access_token=" + access_token

    params = {"group_id": group_id}

    result = url_request(url, header, params)
    return result

def delete_user(group_id,user_id):
    '''
    删除用户：用于将用户从某个组中删除。

    '''

    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/delete" + "?access_token=" + access_token


    params = {"group_id": group_id, "user_id": user_id,}
    result = url_request(url, header, params)

    print( result)


def add_group(group_id):

    '''
    创建用户组 : 用于创建一个空的用户组，如果用户组已存在 则返回错误。

    '''
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/add" + "?access_token=" + access_token

    params = {"group_id":group_id}
    result = url_request(url, header, params)

    print( result)

def delete_group(group_id):
    '''
    删除用户组：删除用户组下所有的用户及人脸，如果组不存在 则返回错误。
。

    '''

    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/delete" + "?access_token=" + access_token


    params = {"group_id": group_id}
    result = url_request(url, header, params)

    print( result)

def get_group_list():
    '''
    组列表查询 : 用于查询用户组的列表。

    '''

    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getlist" + "?access_token=" + access_token



    params = {"start": 0, 'length':100}
    result = url_request(url, header, params)

    print( result)


if __name__ == "__main__":
    group_id = 'paqu'
    #update_face('/Users/androiduser/Desktop/Data/Manual-Label/images_asia/0a20fce0646fe017cc9108d0dc2e7609.jpg',group_id,'0a0d15a7a4fbf24d29667ed60e8','21 50.43471909 none fmale')
    #delete_face('images_96_112','0a1c5022f524ba88a902c2cfe93bb282','0a74a73c44dcd7e98db9197565a664a8')
    #delete_user(group_id,'0a0d15aaaa7a4d5fbf24d29667ed60e8')
    #delete_group(group_id)
    #get_group_list()
    #add_group(group_id)
    #add_face('/Users/androiduser/Desktop/Data/Manual-Label/images_asia/0a02e61c7374ac12747d6459350c5607.jpg',group_id,'0a0d15a7a4fbf24d29667ed60e8','22 40.43471909 none male')
    #print(get_users_list(group_id))

