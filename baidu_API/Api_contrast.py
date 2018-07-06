from baidu_API.APP_info import get_access_token
import urllib3,base64,json, time

from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)



def face_contrast_api(file_path_1, file_path_2):
    start = time.clock()
    access_token=get_access_token()
    http=urllib3.PoolManager()
    IMAGE_TYPE='BASE64'
    url='https://aip.baidubce.com/rest/2.0/face/v3/match?access_token='+access_token
    f1 = open(file_path_1,'rb')
    f2 = open(file_path_2,'rb')
    #参数image：图像base64编码 分别base64编码后的2张图片数据
    img1 = base64.b64encode(f1.read())
    img2 = base64.b64encode(f2.read())
    #params = {"images":str(img1,'utf-8') + ',' + str(img2,'utf-8')}
    params = [{"image":str(img1,'utf-8'),"image_type":IMAGE_TYPE},{"image":str(img2,'utf-8'),"image_type":IMAGE_TYPE}]
    #参数转JSON格式
    encoded_data = json.dumps(params).encode('utf-8')
    request=http.request('POST',
                          url,
                          body=encoded_data,
                          headers={'Content-Type':'application/json'})
    #对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
    result = json.loads(request.data)
    end = time.clock()
    print(end - start)
    return result

if __name__ == '__main__':
    print(face_contrast_api('/Users/androiduser/Desktop/Data/qian/qian/1/image_read.png','/Users/androiduser/Desktop/Data/qian/qian/2/image_read.png'))
    print(face_contrast_api('/Users/androiduser/Desktop/Data/qian/qian/1/image_read.png','/Users/androiduser/Desktop/Data/qian/qian/2/image_read.png'))
    print(face_contrast_api('/Users/androiduser/Desktop/Data/qian/qian/2/image_read.png','/Users/androiduser/Desktop/Data/qian/qian/2/image_read.png'))
    print(face_contrast_api('/Users/androiduser/Desktop/Data/qian/qian/3/image_read.png','/Users/androiduser/Desktop/Data/hou/hou/1/image_read.png'))
    print(face_contrast_api('/Users/androiduser/Desktop/Data/hou/hou/1/image_read.png','/Users/androiduser/Desktop/Data/qian/qian/2/image_read.png'))
    print(face_contrast_api('/Users/androiduser/Desktop/Data/hou/hou/2/image_read.png','/Users/androiduser/Desktop/Data/hou/hou/1/image_read.png'))