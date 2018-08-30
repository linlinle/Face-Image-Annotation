
import base64
from util import url_request,access_token


def face_search(file_path,  group_id_list):

    with open(file_path, 'rb') as f:
        img = base64.b64encode(f.read())

    url='https://aip.baidubce.com/rest/2.0/face/v3/search?access_token='+access_token

    header = 'Content-Type', 'application/json'
    params = {"image":'' + str(img, 'utf-8') + '',"image_type":"BASE64", "group_id_list":group_id_list}

    result = url_request(url,header,params)
    return result

if __name__ == '__main__':
    print(face_search('/Users/androiduser/Desktop/Data/Manual-Label/images_96_112/f3bb50af2e1f47c328f609d6b262b621.jpg','paqu'))