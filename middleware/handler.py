import base64
import json
import os
import random
import time

import requests
import rsa
from pymysql.cursors import DictCursor

from common import yaml_handler, excel_handler, logging_handler,requests_handler
from common.mysql_handler import MysqlHandler
from config import config

key_str = '''
    -----BEGIN PUBLIC KEY-----
    {}
    -----END PUBLIC KEY-----
'''

class MysqlHandlerMid(MysqlHandler):
    """读取配置文件的选项：MysqlHandler"""
    def __init__(self):
        """初始化所有的配置项，从yaml当中读取"""
        db_config = Handler.yaml["db"]

        super().__init__(
            host=db_config["host"],
            port=db_config["port"],
            user=db_config["user"],
            password=db_config["password"],
            charset=db_config["charset"],
            cursorclass=DictCursor
        )

class Handler():
    """初始化所有的数据
    在其他的模块当中重复使用
    是从 common 当中实例化对象
    """
    # 加载 python 配置项
    conf = config

    # YAML 数据
    yaml = yaml_handler.read_yaml(os.path.join(config.CONFIG_PATH, "config.yaml"))

    # 读取excel数据
    __excel_path = conf.DATA_PATH
    __excel_file = yaml["excel"]["file"]
    excel = excel_handler.ExcelHandler(os.path.join(__excel_path,__excel_file))

    # logger
    __logger_config = yaml["logger"]
    logger = logging_handler.get_logger(
        name=__logger_config["name"],
        file = os.path.join(config.LOG_PATH, __logger_config["file"]),
        logger_level=__logger_config["logger_level"],
        stream_level=__logger_config['stream_level'],
        file_level=__logger_config["file_level"]
    )
    db_class = MysqlHandlerMid



    @property
    def token_test1(self):
        return login_test1()["token"]

    @property
    def user_id_test1(self):
        return login_test1()["user_id"]

    @property
    def token_test2(self):
        return login_test2()["token"]

    @property
    def user_id_test2(self):
        return login_test2()["user_id"]

    @property
    def resourceId(self):
        return add_resource()["resourId"]

    @property
    def projectId(self):
        # 联邦资源id
        return add_project()['projectId']

    @property
    def pid(self):
        # 联邦资源id
        return add_project()['pid']




def getkey_test1():
    key_url = "http://test1.primihub.com/prod-api/sys/common/getValidatePublicKey?timestamp=" + str(
            int(time.time())) + "&nonce=" + str(random.randint(0, 9))
    result = requests.get(key_url).json()["result"]
    publicKey = result["publicKey"]
    publicKeyName = result["publicKeyName"]
    pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.format(publicKey).encode())
    passwd = Handler.yaml['user']["userPassword"]
    cryptedMessage = rsa.encrypt(passwd.encode(encoding="utf-8"), pubKey)
    key_str_text = base64.b64encode(cryptedMessage)

    return publicKeyName, key_str_text

def login_test1():
    """登录测试账号"""
    publicKeyName, key_str_text = getkey_test1()
    data1 = {"userAccount":Handler.yaml['user']["userAccount"],
             "validateKeyName":publicKeyName,
             "timestamp":str(int(time.time())),
             "nonce":str(random.randint(0, 9)),
             "userPassword":key_str_text}
    res = requests_handler.visit(
        url=Handler.yaml["host1"]+"/sys/user/login",
        method="post",
        data=data1
    )
    # 提取token、
    token_test1 = res['result']['token']
    user_id_test1 = res["result"]["sysUser"]["userId"]

    return {"token":token_test1,"user_id":user_id_test1}


def getkey_test2():
    key_url = "http://test2.primihub.com/prod-api/sys/common/getValidatePublicKey?timestamp=" + str(
            int(time.time())) + "&nonce=" + str(random.randint(0, 9))
    result = requests.get(key_url).json()["result"]
    publicKey = result["publicKey"]
    publicKeyName = result["publicKeyName"]
    pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.format(publicKey).encode())
    passwd = Handler.yaml['user']["userPassword"]
    cryptedMessage = rsa.encrypt(passwd.encode(encoding="utf-8"), pubKey)
    key_str_text = base64.b64encode(cryptedMessage)

    return publicKeyName, key_str_text

def login_test2():
    """登录测试账号"""
    publicKeyName, key_str_text = getkey_test2()
    data = {"userAccount":Handler.yaml['user']["userAccount"],
             "validateKeyName":publicKeyName,
             "timestamp":str(int(time.time())),
             "nonce":str(random.randint(0, 9)),
             "userPassword":key_str_text}
    res = requests_handler.visit(
        url=Handler.yaml["host3"]+"/sys/user/login",
        method="post",
        data=data
    )
    # 提取token、
    token_test2 = res['result']['token']
    user_id_test2 = res["result"]["sysUser"]["userId"]

    return {"token":token_test2,"user_id":user_id_test2}

def add_resource():
    data:str = '{"resourceName":"111","resourceDesc":"111","tags":["111"],"resourceSource":1,"resourceAuthType":1,"fileId":1161,"fieldList":[{"fieldId":null,"fieldName":"Class","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x0","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x1","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x2","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x3","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x4","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x5","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0}],"fusionOrganList":[],"timestamp":"#timestamp#","nonce":802,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().token_test1)
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))

    resp = requests_handler.visit(
        url=Handler.yaml["host2"] + "/resource/saveorupdateresource",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    resourId = resp["result"]["resourceId"]
    return {"resourId":resourId}

def add_project():
    data:str = '{"serverAddress":"http://fusion:8080/","projectName":"123","projectDesc":"123","projectOrgans":[{"organId":"2cad8338-2e8c-4768-904d-2b598a7e3298","participationIdentity":2,"resourceIds":["2b598a7e3298-599fa154-1e60-4ce2-aea5-092270bf9dd3"]},{"organId":"8bf56ee6-b004-4ada-b078-591acb22b324","participationIdentity":1,"resourceIds":["591acb22b324-82f7821e-900c-40c1-899f-c481fda8cd5e"]}],"timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().token_test1)
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    resp = requests_handler.visit(
        url=Handler.yaml["host2"] + "/project/saveOrUpdateProject",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    projectId = resp['result']['projectId']
    pid = resp['result']['id']
    return {"projectId":projectId,"pid":pid}



if __name__ == "__main__":
    data_path = Handler.conf.DATA_PATH
    # print(Handler.yaml["excel"]["file"])
    # print(Handler.logger)
    # db = MysqlHandlerMid()
    # # print(Handler.userId)
    # # data = db.query("select * from privacy_test1.data_resource where user_id= 4;",one=False)
    # data = db.query("select * from privacy_test1.data_resource where user_id={}".format(Handler().user_id), one=False)
    # print(data)
    print(Handler().token_test1)
    print(Handler().projectId)
    print(Handler().id)
    # print(add_project())
    # print(add_resource())

    # 测试登录函数
    # print(login())
    # print(Handler().token_test1)


