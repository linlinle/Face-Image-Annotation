
import json
import base64
import urllib3
from urllib.parse import urlencode
from APP_info import access_token
from http_request import http_request

from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

def face_search(file_path,  group_id_list):

    '''
    人脸搜索
        1：N人脸识别与1：N人脸认证的差别在于：人脸搜索是在指定人脸集合中进行直接地人脸检索操作，而人脸认证是基于uid，
        先调取这个uid对应的人脸，再在这个uid对应的人脸集合中进行检索（因为每个uid通常对应的只有一张人脸，所以通常也就变为了1：1对比）；
        实际应用中，人脸认证需要用户或系统先输入id，这增加了验证安全度，但也增加了复杂度，具体使用哪个接口需要视您的业务场景判断。


    '''
    with open(file_path, 'rb') as f:
        img = base64.b64encode(f.read())

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"


    params = {"image":'' + str(img, 'utf-8') + '',"image_type":"BASE64", "group_id_list":group_id_list}

    result = http_request(params, request_url)
    print(result)
    return result['result']['user_list']

if __name__ == '__main__':
    face_search('/Users/androiduser/Desktop/Data/Manual-Label/images_96_112/0a74a73c44dcd7e98db9197565a664a8.jpg','images_96_112')