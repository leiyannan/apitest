import base64
import json
import os
import random
import time
from datetime import date


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



    # @property
    # def token_test1(self):
    #     return login_test1()["token"]
    #
    # @property
    # def user_id_test1(self):
    #     return login_test1()["user_id"]
    #
    # @property
    # def token_test2(self):
    #     return login_test2()["token"]
    #
    # @property
    # def user_id_test2(self):
    #     return login_test2()["user_id"]


    @property
    def resourceId01(self):
        # test1本地资源ID
        return add_resource01()["resourceId01"]

    @property
    def resourceFusionId01(self):
        # test1联邦资源ID
        return add_resource01()["resourceFusionId01"]

    @property
    def resourceId02(self):
        # test2本地资源ID
        return add_resource01()["resourceId02"]

    @property
    def resourceFusionId02(self):
        # test2联邦资源ID
        return add_resource02()["resourceFusionId02"]

    @property
    def projectId(self):
        # 联邦项目id
        return add_project()['projectId']

    @property
    def pid(self):
        # 本地项目id
        return add_project()['pid']



# def getkey_test1():
#     key_url = "http://test1.primihub.com/prod-api/sys/common/getValidatePublicKey?timestamp=" + str(
#             int(time.time())) + "&nonce=" + str(random.randint(0, 9))
#     result = requests.get(key_url).json()["result"]
#     publicKey = result["publicKey"]
#     publicKeyName = result["publicKeyName"]
#     pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.format(publicKey).encode())
#     passwd = Handler.yaml['user01']["userPassword"]
#     cryptedMessage = rsa.encrypt(passwd.encode(encoding="utf-8"), pubKey)
#     key_str_text = base64.b64encode(cryptedMessage)
#
#     return publicKeyName, key_str_text

# def login_test1():
#     """登录测试账号"""
#     publicKeyName, key_str_text = getkey_test1()
#     data1 = {"userAccount":Handler.yaml['user01']["userAccount"],
#              "validateKeyName":publicKeyName,
#              "timestamp":str(int(time.time())),
#              "nonce":str(random.randint(0, 9)),
#              "userPassword":key_str_text}
#     res = requests_handler.visit(
#         url=Handler.yaml["host1"]+"/sys/user/login",
#         method="post",
#         data=data1
#     )
#     # 提取token、
#     token_test1 = res['result']['token']
#     user_id_test1 = res["result"]["sysUser"]["userId"]
#
#     return {"token":token_test1,"user_id":user_id_test1}
#
#
# def getkey_test2():
#     key_url = "http://test2.primihub.com/prod-api/sys/common/getValidatePublicKey?timestamp=" + str(
#             int(time.time())) + "&nonce=" + str(random.randint(0, 9))
#     result = requests.get(key_url).json()["result"]
#     publicKey = result["publicKey"]
#     publicKeyName = result["publicKeyName"]
#     pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.format(publicKey).encode())
#     passwd = Handler.yaml['user02']["userPassword"]
#     cryptedMessage = rsa.encrypt(passwd.encode(encoding="utf-8"), pubKey)
#     key_str_text = base64.b64encode(cryptedMessage)
#
#     return publicKeyName, key_str_text
#
# def login_test2():
#     """登录测试账号"""
#     publicKeyName, key_str_text = getkey_test2()
#     data = {"userAccount":Handler.yaml['user02']["userAccount"],
#              "validateKeyName":publicKeyName,
#              "timestamp":str(int(time.time())),
#              "nonce":str(random.randint(0, 9)),
#              "userPassword":key_str_text}
#     res = requests_handler.visit(
#         url=Handler.yaml["host3"]+"/sys/user/login",
#         method="post",
#         data=data
#     )
#     # 提取token、
#     token_test2 = res['result']['token']
#     user_id_test2 = res["result"]["sysUser"]["userId"]
#
#     return {"token":token_test2,"user_id":user_id_test2}

def add_resource01():
    # test1环境添加资源
    data:str = '{"resourceName":"#resourceName#","resourceDesc":"ceasd","tags":["sdf"],"resourceSource":1,"resourceAuthType":1,"fileId":1210,"fieldList":[{"fieldId":null,"fieldName":"Class","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"y","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x1","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x2","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x3","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x4","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x5","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0}],"fusionOrganList":[],"timestamp":#timestamp#,"nonce":248,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#resourceName#" in data:
        data = data.replace("#resourceName#", Handler.yaml["test_name"]["resourceName01"])

    resp = requests_handler.visit(
        url=Handler.yaml["host2"] + "/resource/saveorupdateresource",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    resourceId01 = resp["result"]["resourceId"]
    resourceFusionId01 = resp["result"]["resourceFusionId"]
    return {"resourceId01":resourceId01, "resourceFusionId01":resourceFusionId01}

def add_resource02():
    # test2环境添加资源
    data:str = '{"resourceName":"#resourceName#","resourceDesc":"资源描述","tags":["test"],"resourceSource":1,"resourceAuthType":1,"fileId":1159,"fieldList":[{"fieldId":null,"fieldName":"x6","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x7","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x8","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x9","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x10","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x11","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x12","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0}],"fusionOrganList":[],"timestamp":"#timestamp#","nonce":212,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#resourceName#" in data:
        data = data.replace("#resourceName#", Handler.yaml["test_name"]["resourceName02"])

    resp = requests_handler.visit(
        url=Handler.yaml["host4"] + "/resource/saveorupdateresource",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    resourceId02 = resp["result"]["resourceId"]
    resourceFusionId02 = resp["result"]["resourceFusionId"]
    return {"resourceId02":resourceId02,"resourceFusionId02":resourceFusionId02}

def add_project():
    # 使用test1和test2的新增资源，在test1环境新建项目
    data:str = '{"serverAddress":"#serverAddress#","projectName":"#projectName01#","projectDesc":"new_project","projectOrgans":[{"organId":"#organId02#","participationIdentity":2,"resourceIds":["#resourceFusionId02#"]},{"organId":"#organId01#","participationIdentity":1,"resourceIds":["#resourceFusionId01#"]}],"timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#serverAddress#" in data:
        data = data.replace("#serverAddress#", Handler().yaml["test"]["serverAddress"])
    if "#projectName01#" in data:
        data = data.replace("#projectName01#", Handler().yaml["test_name"]["projectName01"])
    if "#organId01#" in data:
        data = data.replace("#organId01#", Handler().yaml["test"]["organId01"])
    if "#organId02#" in data:
        data = data.replace("#organId02#", Handler().yaml["test"]["organId02"])
    if "#resourceFusionId01#" in data:
        data = data.replace("#resourceFusionId01#", str(Handler.resourceFusionId01))
    if "#resourceFusionId02#" in data:
        data = data.replace("#resourceFusionId02#", str(Handler.resourceFusionId02))
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

def getProjectDetails():
    # test2请求项目详情，获得项目资源真实ID，以便进行项目审核、资源审核
    data = '{"id":"#projectId#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#projectId#" in data:
        data = data.replace("#projectId#", str(Handler().projectId))
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    print(data)

    resp = requests_handler.visit(
        url=Handler.yaml["host4"] + "/project/getProjectDetails",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    #
    return resp


if __name__ == "__main__":
    data_path = Handler.conf.DATA_PATH
    # print(Handler.yaml["excel"]["file"])
    # print(Handler.logger)
    # db = MysqlHandlerMid()
    # # print(Handler.userId)
    # # data = db.query("select * from privacy_test1.data_resource where user_id= 4;",one=False)
    # data = db.query("select * from privacy_test1.data_resource where user_id={}".format(Handler().user_id), one=False)
    # print(data)
    # print(Handler().token_test1)
    # print(Handler().projectId)
    #print(Handler().resourceFusionId01)
    #print(Handler().resourceFusionId02)
    # print(add_project())
    print(getProjectDetails())
    # print(add_resource())

    # 测试登录函数，由于登录加入滑动图片验证码，且错误率高，则使用万能token
    # print(login())
    # print(Handler().token_test1)
    # print(Handler().token_test2)


