
import base64
import json
import os
import time
import random

import requests
import rsa
from pymysql.cursors import DictCursor

from common import yaml_handler, excel_handler, logging_handler,requests_handler
from common.mysql_handler import MysqlHandler
from config import config
from requests_toolbelt import MultipartEncoder


# class add_resource:








def upload_csv_file01(filename):

    binFile = open(os.path.join(config.DATA_PATH, filename), "rb")

    headers = {}
    multipart_encoder = MultipartEncoder(
        fields={
            "file": (filename, binFile.read()),
            "fileSource": "1",
            'timestamp': "1680338065038",
            'nonce': "123",
            'token': Handler.yaml["test"]["token"]
        },
        boundary='----WebKitFormBoundaryJ2aGzfsg35YqeT7X'
    )

    headers['Content-Type'] = multipart_encoder.content_type

    actual = requests_handler.visit(
        url=Handler.yaml["host1"] + '/sys/file/upload',
        data=multipart_encoder,
        headers=headers)
    binFile.close()
    #print(actual)
    filrId01 = actual["result"]["sysFile"]["fileId"]

    data = '{"fileId":"#fileId#","timestamp":"#timestamp#","nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#fileId#" in data:
        data = data.replace("#fileId#", filrId01)
    resp = requests_handler.visit(
        url=Handler.yaml["host1"] + "/data/resource/resourceFilePreview",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    fieldList = resp["result"]["fieldList"]
    filrId = resp["result"]["fieldID"]
    for line in fieldList:
        del line["createDate"]
        del line["fieldAs"]
    fieldList = str(fieldList).replace("'", '"').replace("False", "0").replace("None", "null").replace(" ", "")
    # return fieldList,fileId01

# def add_resource01():
#     fieldList, fileId01 = resourceFilePreview01()
    # test1环境添加资源
    data:str = '{"resourceName":"#resourceName#","resourceDesc":"55555","tags":["555"],"resourceSource":1,"resourceAuthType":1,"fileId":"#fileId01#","fieldList":"#fieldList#","fusionOrganList":[],"timestamp":"#timestamp#","nonce":691,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#fileId01#" in data:
        data = data.replace("#fileId01#", fileId)
    if "#fieldList#" in data:
        data = data.replace("#fieldList#", fieldList)
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#resourceName#" in data:
        data = data.replace("#resourceName#",filename )

    resp = requests_handler.visit(
        url=Handler.yaml["host1"] + "/data/resource/saveorupdateresource",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    print(resp)
    resourceId01 = resp["result"]["resourceId"]
    resourceFusionId01 = resp["result"]["resourceFusionId"]
    print(resourceFusionId01)
    return {"resourceId01":resourceId01, "resourceFusionId01":resourceFusionId01}

