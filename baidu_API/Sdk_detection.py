from aip import AipFace
import base64
from baidu_API.APP_info import AppID,API_Key,Secret_Key
import time


start = time.clock()
client = AipFace(AppID,API_Key,Secret_Key)
f = open('/Users/androiduser/Desktop/Data/Manual-Label/images/0_106944787132087964841162957466821478746.jpg','rb')
image = base64.b64encode(f.read())
image64 = str(image,'utf-8')
requst = client.detect(image64, "BASE64", None)
print(requst)
end = time.clock()
print(end - start)