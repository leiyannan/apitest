import time
import datetime
import hashlib
import os
import random
import sys
import requests
import json

from requests_toolbelt.multipart.encoder import MultipartEncoder
from common import requests_handler, yaml_handler
from config import config
from middleware.handler import Handler
from requests_toolbelt import MultipartEncoder

url = 'http://test1.primihub.com/prod-api/sys/file/upload'

headers ={}

binFile=open("/Users/alei/PycharmProjects/apitest/data/PSI-用户数据B.csv", "rb")


multipart_encoder = MultipartEncoder(
        fields={
            "file":("test.txt",binFile.read()),
            "fileSource":"1",
            'timestamp': "1680338065038",
            'nonce': "123",
            'token': Handler.yaml["test"]["token"]
        },
        boundary='----WebKitFormBoundaryJ2aGzfsg35YqeT7X'
    )
headers['Content-Type']=multipart_encoder.content_type

# print(multipart_encoder)
headers['Content-Type'] = multipart_encoder.content_type
#请求头必须包含一个特殊的头信息，类似于Content-Type: multipart/form-data; boundary=${bound}

print(headers)
responseStr = requests.post(url, data=multipart_encoder, headers=headers)
print(responseStr.text)

