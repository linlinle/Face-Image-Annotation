import json
import urllib3,base64
from urllib.parse import urlencode

from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)



def face_detection(file_path):
    access_token = '24.c97159d812ea83b5824d1754d22f023b.2592000.1533290553.282335-11474874'

    http=urllib3.PoolManager()
    url='https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token='+access_token
    with open(file_path,'rb') as f:

        #参数image：图像base64编码 以及face_fields参数
        #image的值取决于 image_type
        img = base64.b64encode(f.read())

    ##params 把三种值请求都给出了 测试请自己选择是用BASE64 FACE_TOKEN URL哪个。剩下的2个params注释掉 一定要自己看看文档 URL给的那个图片网络地址只是示例并不是一个真正可以访问的图片网络地址
    params={'image':''+str(img,'utf-8')+'','image_type':'BASE64','face_field':'age,beauty,expression,gender'}
    #params={'image':'f7ec8ecd441886371b9749d1fc853f44','image_type':'FACE_TOKEN','face_field':'age,beauty,faceshape,gender,glasses'}
    #params={'image':'https://www.xsshome.cn/face.jpg','image_type':'URL','face_field':'age,beauty,faceshape,gender,glasses'}


    #对base64数据进行urlencode处理
    params=urlencode(params)
    request=http.request('POST',
                          url,
                          body=params,
                          headers={'Content-Type':'application/json'})

    #对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
    result = json.loads(request.data)
    return result

if __name__ == '__main__':
    print(face_detection('/Users/androiduser/Desktop/Data/Manual-Label/image1/75555670682e42f9fd18e5a4af99bb38.jpg'))
