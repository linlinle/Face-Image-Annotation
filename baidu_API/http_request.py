
import json
import urllib3
from urllib.parse import urlencode
from APP_info import access_token

from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


def http_request(params,request_url):
    request_url = request_url + "?access_token=" + access_token
    http=urllib3.PoolManager()
    params=urlencode(params)
    request = http.request('POST',
                           request_url,
                           body=params,
                           headers={'Content-Type': 'application/json'})
    result = json.loads(request.data)

    return result