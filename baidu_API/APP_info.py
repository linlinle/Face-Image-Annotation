
import sys
import ssl
from urllib import request,parse

AppID = '11474874'
API_Key = 'FpXo2M4fYD0tqj7owh0ttzpb'
Secret_Key = 'f6LU7Q6XARHvsFywN2vlc5yKcv0xMbCu'
access_token = '24.c97159d812ea83b5824d1754d22f023b.2592000.1533290553.282335-11474874'


def get_access_token():

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(API_Key,Secret_Key)
    req = request.Request(host)
    req.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = request.urlopen(req)
    #获得请求结果
    content = response.read()
    #结果转化为字符
    content = bytes.decode(content)
    #转化为字典
    content = eval(content[:-1])
    return content['access_token']

if __name__ == "__main__":
    print(get_access_token())
