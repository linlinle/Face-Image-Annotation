"""提供一些关键参数和函数来支持百度API人脸属性检测"""
import urllib
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AppID = '11733300'
API_Key = 'TXbWh4GFWfeGaMdw9ZBDyKxc'
Secret_Key = 'MresMGHnibeRgrR99k2qAg4AUigp9x0R'
# 每隔一个月换一次
access_token = '24.25568f89f46d444c47f81d14a3ecf17b.2592000.1537946999.282335-11733300'


def getAccessToken():
    """
    获取access_token
    :return:
    """

    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(API_Key,Secret_Key)
    header={'Content-Type': 'application/json; charset=UTF-8'}
    content = urllibRequest(url,header)
    return content['access_token']


def urllibRequest(url, header, params=None):
    """
    利用urllib模块，调用API
    :param url:
    :param header:
    :param params:
    :return:
    """

    if params:
        params = urllib.parse.urlencode(params).encode(encoding='UTF8')
        request = urllib.request.Request(url=url, data=params)
    else:
        request = urllib.request.Request(url=url)

    # request对象
    request.add_header(tuple(header.items())[0][0], tuple(header.items())[0][1])
    response = urllib.request.urlopen(request)
    result = json.loads(response.read())

    return result

def urllib3Request(url,header,params=None):
    """
    有时，urllib.request.Request类会出现调用问题，这是备选的调用API方法
    :param url:
    :param header:
    :param params:
    :return:
    """
    http = urllib3.PoolManager()
    params = urllib.parse.urlencode(params).encode(encoding='UTF8')
    request = http.request('POST',
                           url,
                           body=params,
                           headers=header)
    result = json.loads(request.data)
    return result

if __name__ == "__main__":
    print(getAccessToken())
