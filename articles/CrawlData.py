# Through the interface to crawl the result from the website.
# salt and sign will be change. Should update them in time.
import hashlib
import random
import time
import json
import requests


def crawl_data(query):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    client = 'fanyideskweb'
    ran = 'ebSeFb%=XZ%T[KZ)c(sy!'
    salt = str(int(time.time()*1000) + random.randint(1,10))
    sign = hashlib.md5((client + query + salt + ran).encode('utf-8')).hexdigest()

    payload = {'i': query,
               'from': 'AUTO',
               'to': 'AUTO',
               'smartresult': 'dict',
               'client': client,
               'salt': salt,
               'sign': sign,
               'doctype': 'json',
               'Version': 2.1,
               'keyfrom': 'fanyi.web',
               'action': 'FY_BY_CLICKBUTTON',
               'typoResult': 'false'}

    tag = True

    while tag or response.headers['Content-Type'] != 'application/json;charset=utf-8':
        response = requests.post(url, data=payload)
        tag = False

    content = json.loads(response.text)
    return content['translateResult'][0][0]['tgt']