import base64
import urllib,requests
from getRequest import urllibRequest,urllib3Request,access_token



def baiduAPIDetection(file_path, urllibWay):
    """
    百度API人脸属性检测
    :param file_path: 单张照片文件地址
    :return: 包含照片人脸属性的字典
    """
    url='https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token='+access_token

    # 图片转Base64格式
    with open(file_path,'rb') as f:
        img = base64.b64encode(f.read())

    params={'image':''+str(img,'utf-8')+'',
            'image_type':'BASE64',
            'face_field':'age,beauty,expression,gender'             #返回属性选择
            }
    header = {'Content-Type':'application/json'}
    if urllibWay == 0:
        resultdict = urllibRequest(url,header,params)
    else:
        resultdict = urllib3Request(url, header, params)
    return resultdict




if __name__ == '__main__':
    print(face_detection('/Users/androiduser/Desktop/Data/Manual-Label/images_asia/0a2fbc38578a006e3a9803428d9d0aa6.jpg'))