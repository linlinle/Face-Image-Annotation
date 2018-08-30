from util import access_token
import urllib,base64,json



def face_contrast_api(file_path_1, file_path_2):
    url='https://aip.baidubce.com/rest/2.0/face/v3/match?access_token='+access_token
    with open(file_path_1,'rb') as f1:
        img1 = base64.b64encode(f1.read())

    with open(file_path_2,'rb') as f2:
        img2 = base64.b64encode(f2.read())


    params = [{"image":str(img1,'utf-8'),"image_type":'BASE64'},{"image":str(img2,'utf-8'),"image_type":'BASE64'}]
    params = json.dumps(params).encode('utf-8')
    request = urllib.request.Request(url=url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    result = eval(response.read())
    return result


if __name__ == '__main__':
    print(face_contrast_api('/Users/androiduser/Desktop/Data/Manual-Label/images_96_112/0a15da7e8ade6394b2709b071f18d8f0.jpg',
                            '/Users/androiduser/Desktop/Data/Manual-Label/images_96_112/0ac8adb964f08eab219655ec4763dc58.jpg'))