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
    def token01(self):
        return login_test(host1)["token"]

    @property
    def token02(self):
        return login_test(host2)["token"]

    @property
    def token03(self):
        return login_test(host3)["token"]


    @property
    def user_id01(self):
        return login_test(host1)["user_id"]

    @property
    def user_id02(self):
        return login_test(host2)["user_id"]

    @property
    def user_id03(self):
        return login_test(host3)["user_id"]

   # 获取机构ID、name和中心节点地址
    @property
    def organId01(self):
        return getLocalOrganInfo(host1)[0]

    @property
    def organId02(self):
        return getLocalOrganInfo(host2)[0]

    @property
    def organId03(self):
        return getLocalOrganInfo(host3)[0]

    @property
    def organName01(self):
        return getLocalOrganInfo(host1)[1]

    @property
    def organName02(self):
        return getLocalOrganInfo(host2)[1]

    @property
    def organName03(self):
        return getLocalOrganInfo(host3)[1]

    @property
    def publicKey(self):
        # test1公钥
        return getLocalOrganInfo(host1)[2]

    # host123上传文件分别获取fileId
    @property
    def fileId01(self):
        return add_resource(host=host1)["fileId"]

    @property
    def fileId02(self):
        return add_resource(host=host2)["fileId"]

    @property
    def fileId03(self):
        return add_resource(host=host3)["fileId"]


    # host123上传文件分别获取fieldList
    @property
    def fieldList01(self):
        return add_resource(host=host1)["fieldList"]

    @property
    def fieldList02(self):
        return add_resource(host=host2)["fieldList"]

    @property
    def fieldList03(self):
        return add_resource(host=host3)["fieldList"]

    # host123上传资源分别获取本地资源ID
    @property
    def resourceId01(self):
        return add_resource(host=host1)["resourceId"]
    @property
    def resourceId02(self):
        return add_resource(host=host2)["resourceId"]
    @property
    def resourceId03(self):
        return add_resource(host = host3)["resourceId"]

    # host1--注册各项任务的测试数据--host方--本地资源ID
    @property
    def train_xgb_host(self):
        return add_resource(host= host1,filename=Handler.yaml["test_data"]["train_xgb_host"])["resourceId"]
    @property
    def test_xgb_host(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["test_v_host"])["resourceId"]

    @property
    def train_lr_host(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["train_lr_host"])["resourceId"]
    @property
    def test_lr_host(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["test_lr"])["resourceId"]

    @property
    def train_lrnn_host(self):
        return add_resource(host=host1,filename=Handler.yaml["test_data"]["train_lrnn_host"])["resourceId"]

    @property
    def test_lrnn_host(self):
        return add_resource(host=host1,filename=Handler.yaml["test_data"]["test_lrnn"])["resourceId"]


    @property
    def train_mpc_01(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["mpc_lr_01"])["resourceId"]

    @property
    def psi_a(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["psi_a"])["resourceId"]

    # host2--注册各项任务的测试数据--guest方
    @property
    def train_xgb_guest(self):
        return add_resource(host= host2,filename=Handler.yaml["test_data"]["train_xgb_guest"])["resourceId"]

    @property
    def test_xgb_guest(self):
        return add_resource(host= host2,filename=Handler.yaml["test_data"]["test_v_guest"])["resourceId"]

    @property
    def train_lr_guest(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["train_lr_guest"])["resourceId"]

    @property
    def test_lr_guest(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["test_lr"])["resourceId"]

    @property
    def train_lrnn_guest(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["train_lrnn_guest"])["resourceId"]

    @property
    def test_lrnn_guest(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["test_lrnn"])["resourceId"]

    @property
    def train_mpc_02(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["mpc_lr_02"])["resourceId"]

    @property
    def psi_b(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["psi_b"])["resourceId"]

    @property
    def pir_data(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["pir_data"])["resourceId"]

    # host3--注册各项任务的测试数据--guest方
    @property
    def train_mpc_03(self):
        return add_resource(host=host3, filename=Handler.yaml["test_data"]["mpc_lr_03"])["resourceId"]





    # host123上传资源分别获取联邦资源ID
    @property
    def resourceFusionId01(self):
        return add_resource(host = host1)["resourceFusionId"]

    @property
    def resourceFusionId02(self):
        return add_resource(host = host2)["resourceFusionId"]

    @property
    def resourceFusionId03(self):
        return add_resource(host = host3)["resourceFusionId"]

    # host1--注册各项任务的测试数据--host方--本地资源ID
    @property
    def train_xgb_host_FusionId(self):
        return add_resource(host= host1,filename=Handler.yaml["test_data"]["train_xgb_host"])["resourceFusionId"]

    @property
    def test_xgb_host_FusionId(self):
        return add_resource(host= host1,filename=Handler.yaml["test_data"]["test_v_host"])["resourceFusionId"]

    @property
    def train_lr_host_FusionId(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["train_lr_host"])["resourceFusionId"]

    @property
    def test_lr_host_FusionId(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["test_lr"])["resourceFusionId"]

    @property
    def train_lrnn_host_FusionId(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["train_lrnn_host"])["resourceFusionId"]

    @property
    def test_lrnn_host_FusionId(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["test_lrnn"])["resourceFusionId"]

    @property
    def train_mpc_01_FusionId(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["mpc_lr_01"])["resourceFusionId"]

    @property
    def psi_a_FusionId(self):
        return add_resource(host=host1, filename=Handler.yaml["test_data"]["psi_a"])["resourceFusionId"]

    # host2--注册各项任务的测试数据--guest方
    @property
    def train_xgb_guest_FusionId(self):
        return add_resource(host= host2,filename=Handler.yaml["test_data"]["train_xgb_guest"])["resourceFusionId"]

    @property
    def test_xgb_guest_FusionId(self):
        return add_resource(host= host2,filename=Handler.yaml["test_data"]["test_v_guest"])["resourceFusionId"]

    @property
    def train_lr_guest_FusionId(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["train_lr_guest"])["resourceFusionId"]

    @property
    def test_lr_guest_FusionId(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["test_lr"])["resourceFusionId"]

    @property
    def train_lrnn_guest_FusionId(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["train_lrnn_guest"])["resourceFusionId"]

    @property
    def test_lrnn_guest_FusionId(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["test_lrnn"])["resourceFusionId"]

    @property
    def train_mpc_02_FusionId(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["mpc_lr_02"])["resourceFusionId"]

    @property
    def psi_b_FusionId(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["psi_b"])["resourceFusionId"]

    @property
    def pir_data_FusionId(self):
        return add_resource(host=host2, filename=Handler.yaml["test_data"]["pir_data"])["resourceFusionId"]

    # host3--注册各项任务的测试数据--第三方
    @property
    def train_mpc_03_FusionId(self):
        return add_resource(host=host3, filename=Handler.yaml["test_data"]["mpc_lr_03"])["resourceFusionId"]



    @property
    def projectId(self):
        # 新创建的未审核host1联邦项目id
        return add_project()[0]

    @property
    def pid01(self):
        # 获取host1已审核的项目本地ID
        return Projectapproval()

    @property
    def pid02(self):
        # test2本地项目id
        return getProjectDetails()[1]

    @property
    def resultId(self):
        # 获取host2本地资源ID
        return getProjectDetails()[0]




host1 = Handler.yaml["host1"]
host2 = Handler.yaml["host2"]
host3 = Handler.yaml["host3"]

# 登录，获取登录token及用户ID
def login_test(host):
    key_url = host + "/sys/common/getValidatePublicKey?timestamp=" + str(
            int(time.time())) + "&nonce=" + str(random.randint(0, 9))
    result = requests.get(key_url).json()["result"]
    publicKey = result["publicKey"]
    publicKeyName = result["publicKeyName"]
    pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.format(publicKey).encode())
    passwd =Handler.yaml['user']["userPassword"]
    cryptedMessage = rsa.encrypt(passwd.encode(encoding="utf-8"), pubKey)
    key_str_text = base64.b64encode(cryptedMessage)


    data = {"userAccount":Handler.yaml['user']["userAccount"],# Handler.yaml['user01']["userAccount"]
             "validateKeyName":publicKeyName,
             "timestamp":str(int(time.time())),
             "nonce":str(random.randint(0, 9)),
             "userPassword":key_str_text
             }
    res = requests_handler.visit(
        url=host+"/sys/user/login",
        method="post",
        data=data
    )
    # 提取token、
    # print(res)
    token_test = res['result']['token']
    user_id = res["result"]["sysUser"]["userId"]

    return {"token":token_test,"user_id":user_id}


def getLocalOrganInfo(host):
    #获取当前环境的机构ID级中心节点地址
    host1 = Handler.yaml["host1"]
    host2 = Handler.yaml["host2"]
    host3 = Handler.yaml["host3"]
    token = login_test(host)["token"]

    data = '{"timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", token)
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))

    resp = requests_handler.visit(
        url=host + "/sys/organ/getLocalOrganInfo",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    # print(resp)
    organId = resp["result"]["sysLocalOrganInfo"]["organId"]
    organName = resp["result"]["sysLocalOrganInfo"]["organName"]
    publicKey = resp["result"]["sysLocalOrganInfo"]["publicKey"]

    return organId,organName,publicKey



def add_resource(host ,filename="训练_纵向xgb_lr_host.csv"):
    timestamp = str(int(time.time()))
    host1 = Handler.yaml["host1"]
    host2 = Handler.yaml["host2"]
    host3 = Handler.yaml["host3"]
    token = login_test(host)["token"]

    # 上传文件
    binFile = open(os.path.join(config.DATA_PATH, filename), "rb")

    headers = {}
    multipart_encoder = MultipartEncoder(
        fields={
            "file": (filename, binFile.read()),
            "fileSource": "1",
            'timestamp': timestamp,
            'nonce': "123",
            'token': token
        },
        boundary='----WebKitFormBoundaryJ2aGzfsg35YqeT7X'
    )
    binFile.close()

    headers['Content-Type'] = multipart_encoder.content_type

    actual = requests_handler.visit(
        url=host + '/sys/file/upload',
        data=multipart_encoder,
        headers=headers)

    fileId = actual["result"]["sysFile"]["fileId"]

    # 获取fieldList
    data = '{"fileId":"#fileId#","timestamp":"#timestamp#","nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", token)
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", timestamp)
    if "#fileId#" in data:
        data = data.replace("#fileId#", str(fileId))
    resp = requests_handler.visit(
        url=host + "/data/resource/resourceFilePreview",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    fieldList = resp["result"]["fieldList"]
    fileId = resp["result"]["fileId"]
    for line in fieldList:
        del line["createDate"]
        del line["fieldAs"]
    fieldList = str(fieldList).replace("'", '"').replace("False", "0").replace("None", "null").replace(" ", "")

    # 添加资源--提交
    data:str = '{"resourceName":"#resourceName#","resourceDesc":"55555","tags":["555"],"resourceSource":1,"resourceAuthType":1,"fileId":#fileId01#,"fieldList":#fieldList#,"fusionOrganList":[],"timestamp":"#timestamp#","nonce":691,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", token)
    if "#fileId01#" in data:
        data = data.replace("#fileId01#", str(fileId))
    if "#fieldList#" in data:
        data = data.replace("#fieldList#", fieldList)
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", timestamp)
    if "#resourceName#" in data:
        data = data.replace("#resourceName#",filename )

    resp02 = requests_handler.visit(
        url=host + "/data/resource/saveorupdateresource",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    print(resp02)
    resourceId = resp02["result"]["resourceId"]
    resourceFusionId = resp02["result"]["resourceFusionId"]
    #print(resourceFusionId)
    return {"host":host,"resourceId":resourceId, "resourceFusionId":resourceFusionId,"fileId":fileId,"fieldList":fieldList}


def add_project():
    # 使用host1和host2、host3的新增资源，并使用该资源 在host1环境新建项目
    data:str = '{"projectName": "测试项目","projectDesc": "测试项目","projectOrgans": [{"organId": "#organId02#","participationIdentity": 2,"resourceIds": ["#train_xgb_guest_FusionId#", "#test_xgb_guest_FusionId#", "#train_lr_guest_FusionId#", "#test_lr_guest_FusionId#", "#train_lrnn_guest_FusionId#","#test_lrnn_guest_FusionId#","#train_mpc_02_FusionId#"]}, {"organId": "#organId03#","participationIdentity": 2,"resourceIds": ["#train_mpc_03_FusionId#"]}, {"organId": "#organId01#","participationIdentity": 1,"resourceIds": ["#train_xgb_host_FusionId#", "#test_xgb_host_FusionId#", "#train_lr_host_FusionId#", "#test_lr_host_FusionId#", "#train_lrnn_host_FusionId#","#test_lrnn_host_FusionId#","#train_mpc_01_FusionId#"]}],"timestamp": #timestamp#,"nonce": 439,"token": "#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().token01)
    if "#organId01#" in data:
        data = data.replace("#organId01#", str(Handler().organId01))
    if "#organId02#" in data:
        data = data.replace("#organId02#", str(Handler().organId02))
    if "#organId03#" in data:
        data = data.replace("#organId03#", str(Handler().organId03))

    if "#train_xgb_host_FusionId#" in data:
        data = data.replace("#train_xgb_host_FusionId#", str(Handler().train_xgb_host_FusionId))
    if "#test_xgb_host_FusionId#" in data:
        data = data.replace("#test_xgb_host_FusionId#", str(Handler().test_xgb_host_FusionId))

    if "#train_lr_host_FusionId#" in data:
        data = data.replace("#train_lr_host_FusionId#", str(Handler().train_lr_host_FusionId))
    if "#test_lr_host_FusionId#" in data:
        data = data.replace("#test_lr_host_FusionId#", str(Handler().test_lr_host_FusionId))
    if "#train_lrnn_host_FusionId#" in data:
        data = data.replace("#train_lrnn_host_FusionId#", str(Handler().train_lrnn_host_FusionId))
    if "#test_lrnn_host_FusionId#" in data:
        data = data.replace("#test_lrnn_host_FusionId#", str(Handler().test_lrnn_host_FusionId))

    if "#train_mpc_01_FusionId#" in data:
        data = data.replace("#train_mpc_01_FusionId#", str(Handler().train_mpc_01_FusionId))
    if "#train_xgb_guest_FusionId#" in data:
        data = data.replace("#train_xgb_guest_FusionId#", str(Handler().train_xgb_guest_FusionId))
    if "#test_xgb_guest_FusionId#" in data:
        data = data.replace("#test_xgb_guest_FusionId#", str(Handler().test_xgb_guest_FusionId))
    if "#train_lr_guest_FusionId#" in data:
        data = data.replace("#train_lr_guest_FusionId#", str(Handler().train_lr_guest_FusionId))
    if "#test_lr_guest_FusionId#" in data:
        data = data.replace("#test_lr_guest_FusionId#", str(Handler().test_lr_guest_FusionId))
    if "#train_lrnn_guest_FusionId#" in data:
        data = data.replace("#train_lrnn_guest_FusionId#", str(Handler().train_lrnn_guest_FusionId))
    if "#test_lrnn_guest_FusionId#" in data:
        data = data.replace("#test_lrnn_guest_FusionId#", str(Handler().test_lrnn_guest_FusionId))
    if "#train_mpc_02_FusionId#" in data:
        data = data.replace("#train_mpc_02_FusionId#", str(Handler().train_mpc_02_FusionId))
    if "#train_mpc_03_FusionId#" in data:
        data = data.replace("#train_mpc_03_FusionId#", str(Handler().train_mpc_03_FusionId))

    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    # print(data)
    resp = requests_handler.visit(
        url= Handler.yaml["host1"] + "/data/project/saveOrUpdateProject",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    projectId = resp['result']['projectId']
    pid01 = resp['result']['id']
    return projectId,pid01


def getProjectDetails():
    host2 = Handler.yaml["host2"]
    host3 = Handler.yaml["host3"]
    timestamp = str(int(time.time()))
    projectId,pid01 = add_project()

    # test2、3请求项目列表，获得第一条项目的本地ID，以便进行项目详情接口请求
    pid=[]
    resourcesid=[]
    organId=[]
    host = [host2,host3]
    for item in host:
        token = login_test(item)["token"]
        data = '{"pageNo":1,"pageSize":10,"timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
        if "#timestamp#" in data:
            data = data.replace("#timestamp#", timestamp)
        if "#token#" in data:
            data = data.replace("#token#", token)
        #print(data)
        resp = requests_handler.visit(
            url=item + "/data/project/getProjectList",
            method="get",
            # headers=json.loads(test_info["header"]),
            params=json.loads(data)
        )
        list = resp["result"]["data"]
        projectid02 = []
        for dict in list:
            projectid02.append(dict["projectId"])
        pid_key = projectid02.index(str(projectId))
        pid02=list[pid_key]["id"]

        # host2、3请求项目详情，获得项目中使用host2资源的本地ID，以便进行项目审核、资源审核
        data = '{"id":"#pid02#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
        if "#timestamp#" in data:
            data = data.replace("#timestamp#", timestamp)
        if "#pid02#" in data:
            data = data.replace("#pid02#", str(pid02))
        if "#token#" in data:
            data = data.replace("#token#", token)

        resp = requests_handler.visit(
            url=item + "/data/project/getProjectDetails",
            method="get",
            # headers=json.loads(test_info["header"]),
            params=json.loads(data)
        )
        #print(resp)
        #获取host2联邦资源ID
        resources = resp["result"]["organs"][1]["resources"]
        id = []
        for i in resources:
            id.append(i["id"])

        resourcesid.append(id)
        # 获取host2本地机构ID
        Id = resp["result"]["organs"][1]["id"]
        organId.append(Id)
        pid.append(pid02)
        #print(resourcesid,organId,pid01,pid)
    return resourcesid,organId,pid01,pid

#
def Projectapproval():
    host2 = Handler.yaml["host2"]
    host3 = Handler.yaml["host3"]
    timestamp = str(int(time.time()))
    resourcesid, organId, pid01,pid = getProjectDetails()

    # 审核项目及资源
    host = [host2,host3]
    for item in host:
        token = login_test(item)["token"]
        if item == host2:
            data = '{"type":"#type#","id":"#id#","auditStatus":1,"auditOpinion":"审核项目&资源","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
            if "#timestamp#" in data:
                data = data.replace("#timestamp#", timestamp)
            if "#token#" in data:
                data = data.replace("#token#", token)

            projectdata = data.replace("#type#", str(1))
            projectdata = projectdata.replace("#id#", str(organId[0]))

            # resourcedata = data.replace("#type#", str(2))
            # 审核项目--同意
            resp01 = requests_handler.visit(
                url=item+ "/data/project/approval",
                method="post",
                data=json.loads(projectdata)
            )
            # print(resp01)

            # 审核资源---同意
            for item2 in resourcesid[0]:
                resp02 = requests_handler.visit(
                    url=item + "/data/project/approval",
                    method="post",
                    data={"type":2,"id":item2,"auditStatus":1,"auditOpinion":"审核项目&资源","timestamp":str(int(time.time())),"nonce":622,"token":token}
                )

        else:
            data = '{"type":"#type#","id":"#id#","auditStatus":1,"auditOpinion":"审核项目&资源","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
            if "#timestamp#" in data:
                data = data.replace("#timestamp#", timestamp)
            if "#token#" in data:
                data = data.replace("#token#", token)

            projectdata = data.replace("#type#", str(1))
            projectdata = projectdata.replace("#id#", str(organId[1]))

            # resourcedata = data.replace("#type#", str(2))
            # 审核项目--同意
            resp01 = requests_handler.visit(
                url=item + "/data/project/approval",
                method="post",
                data=json.loads(projectdata)
            )
            # print(resp01)

            # 审核资源---同意
            for item2 in resourcesid[1]:
                resp02 = requests_handler.visit(
                    url=item + "/data/project/approval",
                    method="post",
                    data={"type": 2, "id": item2, "auditStatus": 1, "auditOpinion": "审核项目&资源",
                          "timestamp": str(int(time.time())), "nonce": 622, "token": token}
                )
    return pid01


def getModel_vel():
    token = Handler().token01
    timestamp = str(int(time.time()))
    projectId = Projectapproval()
    modelId_save = {"xgb_modelId":"xgb_modelId","hlr_modelId":"hlr_modelId","mpc_modelId":"mpc_modelId"}

    requests_data = '{"projectId":"#projectId#","organId":"#organId#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#timestamp#" in requests_data:
        requests_data = requests_data.replace("#timestamp#", timestamp)
    if "#projectId#" in requests_data:
        requests_data = requests_data.replace("#projectId#", str(projectId))
    if "#token#" in requests_data:
        requests_data = requests_data.replace("#token#", token)

    requests_data01 = requests_data.replace("#organId#", str(Handler().organId01))
    requests_data02 = requests_data.replace("#organId#", str(Handler().organId02))
    requests_data03 = requests_data.replace("#organId#", str(Handler().organId03))

    result01 = requests_handler.visit(
        url = Handler.yaml["host1"] + "/data/project/getProjectResourceData",
        method="get",
        params=json.loads(requests_data01)
    )["result"]

    result02 = requests_handler.visit(
        url = Handler.yaml["host1"] + "/data/project/getProjectResourceData",
        method="get",
        params=json.loads(requests_data02)
    )["result"]

    result03 = requests_handler.visit(
        url = Handler.yaml["host1"] + "/data/project/getProjectResourceData",
        method="get",
        params=json.loads(requests_data03)
    )["result"]


    xgb_val = []
    hlr_val = []
    mpclr_val = []
    lrnn_val = []

    for dict01 in result01:
        if Handler.yaml["test_data"]["train_xgb_host"] == dict01["resourceName"]:
            xgb_host_val = {'organId': str(dict01["organId"]),'resourceId': str(dict01["resourceId"]),'resourceName': dict01["resourceName"],
                            'resourceRowsCount': dict01["resourceRowsCount"], 'resourceColumnCount': dict01["resourceColumnCount"],
                            'resourceContainsY': dict01["resourceContainsY"], 'auditStatus': dict01["auditStatus"],
                            'participationIdentity': dict01["participationIdentity"],'fileHandleField':dict01["fileHandleField"],
                            'calculationField':dict01["fileHandleField"],'derivation': str(dict01["derivation"])}
            xgb_val.append(xgb_host_val)

        if Handler.yaml["test_data"]["train_lr_host"] == dict01["resourceName"]:
            hlr_host_val = {'organId': str(dict01["organId"]),'resourceId': str(dict01["resourceId"]),'resourceName': dict01["resourceName"],
                            'resourceRowsCount': dict01["resourceRowsCount"], 'resourceColumnCount': dict01["resourceColumnCount"],
                            'resourceContainsY': dict01["resourceContainsY"], 'auditStatus': dict01["auditStatus"],
                            'participationIdentity': dict01["participationIdentity"],'fileHandleField':dict01["fileHandleField"],
                            'calculationField':dict01["fileHandleField"],'derivation': str(dict01["derivation"])}
            hlr_val.append(hlr_host_val)


        if Handler.yaml["test_data"]["train_lrnn_host"] == dict01["resourceName"]:
            lrnn_host_val = {'organId': str(dict01["organId"]),'resourceId': str(dict01["resourceId"]),'resourceName': dict01["resourceName"],
                            'resourceRowsCount': dict01["resourceRowsCount"], 'resourceColumnCount': dict01["resourceColumnCount"],
                            'resourceContainsY': dict01["resourceContainsY"], 'auditStatus': dict01["auditStatus"],
                            'participationIdentity': dict01["participationIdentity"],'fileHandleField':dict01["fileHandleField"],
                            'calculationField':dict01["fileHandleField"],'derivation': str(dict01["derivation"])}
            lrnn_val.append(lrnn_host_val)

        if Handler.yaml["test_data"]["mpc_lr_01"] == dict01["resourceName"]:
            mpclr_01_val = {'organId': str(dict01["organId"]),'resourceId': str(dict01["resourceId"]),'resourceName': dict01["resourceName"],
                            'resourceRowsCount': dict01["resourceRowsCount"], 'resourceColumnCount': dict01["resourceColumnCount"],
                            'resourceContainsY': dict01["resourceContainsY"], 'auditStatus': dict01["auditStatus"],
                            'participationIdentity': dict01["participationIdentity"],'fileHandleField':dict01["fileHandleField"],
                            'calculationField':dict01["fileHandleField"],'derivation': str(dict01["derivation"])}

            mpclr_val.append(mpclr_01_val)
    # return train_xgb_host,train_lr_host,mpc_lr_01

    for dict02 in result02:
        if Handler.yaml["test_data"]["train_xgb_guest"] == dict02["resourceName"]:
            xgb_guest_val = {'organId': str(dict02["organId"]),'resourceId':str(dict02["resourceId"]),'organName' : str(Handler().organName02),'resourceName': str(dict02["resourceName"]),
                            'resourceRowsCount': dict02["resourceRowsCount"], 'resourceColumnCount': dict02["resourceColumnCount"],
                            'resourceContainsY': dict02["resourceContainsY"], 'auditStatus': dict02["auditStatus"],
                            'participationIdentity': dict02["participationIdentity"],'fileHandleField':dict02["fileHandleField"] ,
                            'calculationField':dict02["fileHandleField"],'derivation': str(dict02["derivation"])}
            xgb_val.append(xgb_guest_val)

        if Handler.yaml["test_data"]["train_lr_guest"] == dict02["resourceName"]:
            hlr_guest_val = {'organId': str(dict02["organId"]), 'organName' : str(Handler().organName02),'resourceId': str(dict02["resourceId"]),
                             'resourceName': str(dict02["resourceName"]),
                             'resourceRowsCount': dict02["resourceRowsCount"],
                             'resourceColumnCount': dict02["resourceColumnCount"],
                             'resourceContainsY': dict02["resourceContainsY"], 'auditStatus': dict02["auditStatus"],
                             'participationIdentity': dict02["participationIdentity"],
                             'fileHandleField': dict02["fileHandleField"],
                             'calculationField': dict02["fileHandleField"], 'derivation': str(dict02["derivation"])}
            hlr_val.append(hlr_guest_val)

        if Handler.yaml["test_data"]["train_lrnn_guest"] == dict02["resourceName"]:
            lrnn_guest_val = {'organId': str(dict02["organId"]), 'organName' : str(Handler().organName02),'resourceId': str(dict02["resourceId"]),
                             'resourceName': str(dict02["resourceName"]),
                             'resourceRowsCount': dict02["resourceRowsCount"],
                             'resourceColumnCount': dict02["resourceColumnCount"],
                             'resourceContainsY': dict02["resourceContainsY"], 'auditStatus': dict02["auditStatus"],
                             'participationIdentity': dict02["participationIdentity"],
                             'fileHandleField': dict02["fileHandleField"],
                             'calculationField': dict02["fileHandleField"], 'derivation': str(dict02["derivation"])}
            lrnn_val.append(lrnn_guest_val)


        if Handler.yaml["test_data"]["mpc_lr_02"] == dict02["resourceName"]:
            mpclr_02_val = {'organId': str(dict02["organId"]), 'organName' : str(Handler().organName02),'resourceId': str(dict02["resourceId"]),
                             'resourceName': str(dict02["resourceName"]),
                             'resourceRowsCount': dict02["resourceRowsCount"],
                             'resourceColumnCount': dict02["resourceColumnCount"],
                             'resourceContainsY': dict02["resourceContainsY"], 'auditStatus': dict02["auditStatus"],
                             'participationIdentity': dict02["participationIdentity"],
                             'fileHandleField': dict02["fileHandleField"],
                             'calculationField': dict02["fileHandleField"], 'derivation': str(dict02["derivation"])}
            mpclr_val.append(mpclr_02_val)


    for dict03 in result03:
        if Handler.yaml["test_data"]["mpc_lr_03"] == dict03["resourceName"]:
            mpclr_03_val = {'organId': str(dict03["organId"]), 'organName' : str(Handler().organName03),'resourceId': str(dict03["resourceId"]),
                            'resourceName': str(dict03["resourceName"]),
                            'resourceRowsCount': dict03["resourceRowsCount"],
                            'resourceColumnCount': dict03["resourceColumnCount"],
                            'resourceContainsY': dict03["resourceContainsY"], 'auditStatus': dict03["auditStatus"],
                            'participationIdentity': dict03["participationIdentity"],
                            'fileHandleField': dict03["fileHandleField"],
                            'calculationField': dict03["fileHandleField"], 'derivation': str(dict03["derivation"])}
            mpclr_val.append(mpclr_03_val)

    return {"projectId":projectId,"xgb_val":xgb_val,"hlr_val":hlr_val,"lrnn_val":lrnn_val,"mpclr_val":mpclr_val}




def runTask():
    token = Handler().token01
    timestamp = str(int(time.time()))
    Model_vel = getModel_vel()

    xgb_data: str = {"param": {"projectId": str(Model_vel["projectId"]), "isDraft": 1, "modelComponents": [
        {"frontComponentId": "0c894164-cc3f-4812-8a13-16ace76ebb6b", "coordinateX": 710, "coordinateY": 100,
         "width": 120, "height": 40, "shape": "start-node",
         "componentCode": "start", "componentName": "开始",
         "componentValues": [{"key": "taskName", "val": "纵向xgb任务"}, {"key": "taskDesc", "val": "纵向xgb任务"}], "input": [],
         "output": [
             {"frontComponentId": "4c98af0b-277e-4f74-9d52-7e4e94390d37", "componentCode": "dataSet",
              "componentName": "选择数据集", "portId": "port1", "pointType": "edge", "pointJson": ""}]},
        {"frontComponentId": "4c98af0b-277e-4f74-9d52-7e4e94390d37", "coordinateX": 650, "coordinateY": 250,
         "width": 180, "height": 50, "shape": "dag-node",
         "componentCode": "dataSet", "componentName": "选择数据集",
         "componentValues": [{"key": "selectData", "val": json.dumps(Model_vel["xgb_val"])}],
         "input": [{"frontComponentId": "0c894164-cc3f-4812-8a13-16ace76ebb6b", "componentCode": "start",
                    "componentName": "开始", "portId": "port2", "pointType": "edge", "pointJson": ""}],
         "output": [{"frontComponentId": "eb315941-fbb1-4988-8808-fb887827362d", "componentCode": "model",
                     "componentName": "模型选择", "portId": "port1", "pointType": "edge", "pointJson": ""}]},
        {"frontComponentId": "eb315941-fbb1-4988-8808-fb887827362d", "coordinateX": 650, "coordinateY": 413,
         "width": 180, "height": 50, "shape": "dag-node", "componentCode": "model", "componentName": "模型选择",
         "componentValues": [{"key": "modelType", "val": "2"},
                             {"key": "numTree", "val": 5}, {"key": "maxDepth", "val": 5},
                             {"key": "regLambda", "val": "1"}, {"key": "minChildWeight", "val": 3},
                             {"key": "isEncrypted", "val": "true"}, {"key": "mergeGh", "val": "true"},
                             {"key": "rayGroup", "val": "true"}, {"key": "sampleType", "val": "random"},
                             {"key": "featureSample", "val": "true"}, {"key": "modelName", "val": "纵向xgb模型"},
                             {"key": "modelDesc", "val": "纵向xgb模型"}],
         "input": [{"frontComponentId": "4c98af0b-277e-4f74-9d52-7e4e94390d37", "componentCode": "dataSet",
                    "componentName": "选择数据集", "portId": "port2", "pointType": "edge", "pointJson": ""}], "output": []}],
                               "modelPointComponents": [{
                                   "frontComponentId": "d1804655-6591-4962-9dc2-753323f83346", "shape": "edge",
                                   "input": {"cell": "0c894164-cc3f-4812-8a13-16ace76ebb6b", "port": "port2"},
                                   "output": {"cell": "4c98af0b-277e-4f74-9d52-7e4e94390d37", "port": "port1"}},
                                   {"frontComponentId": "9a924166-e20f-4f0e-acd2-0186caff9364", "shape": "edge",
                                    "input": {"cell": "4c98af0b-277e-4f74-9d52-7e4e94390d37",
                                              "port": "port2"},
                                    "output": {"cell": "eb315941-fbb1-4988-8808-fb887827362d", "port": "port1"}}]},
                     "timestamp": timestamp, "nonce": 729, "token": token}

    hlr_data: str = {"param": {"projectId": str(Model_vel["projectId"]), "isDraft": 1, "modelComponents": [
        {"frontComponentId": "0770c4ae-c9ba-4e7f-a27e-903fcf3109e5", "coordinateX": 710, "coordinateY": 100,
         "width": 120, "height": 40, "shape": "start-node", "componentCode": "start", "componentName": "开始",
         "componentValues": [{"key": "taskName", "val": "横向lr-DPSGD"}, {"key": "taskDesc", "val": "横向lr-DPSGD"}],
         "input": [], "output": [
            {"frontComponentId": "15ac0fc2-b40c-4f4e-8d09-8507657ea4c2", "componentCode": "dataSet",
             "componentName": "选择数据集", "portId": "port1", "pointType": "edge", "pointJson": ""}]},
        {"frontComponentId": "15ac0fc2-b40c-4f4e-8d09-8507657ea4c2", "coordinateX": 680, "coordinateY": 227,
         "width": 180, "height": 50, "shape": "dag-node", "componentCode": "dataSet", "componentName": "选择数据集",
         "componentValues": [{"key": "selectData", "val": json.dumps(Model_vel["hlr_val"])}], "input": [
            {"frontComponentId": "0770c4ae-c9ba-4e7f-a27e-903fcf3109e5", "componentCode": "start",
             "componentName": "开始", "portId": "port2", "pointType": "edge", "pointJson": ""}],
         "output": [{"frontComponentId": "381c6a40-c09b-448c-b065-700e0c3886f5", "componentCode": "model",
                     "componentName": "模型选择", "portId": "port1", "pointType": "edge", "pointJson": ""}]},
        {"frontComponentId": "381c6a40-c09b-448c-b065-700e0c3886f5", "coordinateX": 660, "coordinateY": 390,
         "width": 180, "height": 50, "shape": "dag-node", "componentCode": "model", "componentName": "模型选择",
         "componentValues": [{"key": "modelType", "val": "3"},
                             {"key": "arbiterOrgan", "val": "c8770d1e-d34d-48d7-bd83-a00c426fd4d3"},
                             {"key": "encryption", "val": "DPSGD"}, {"key": "delta", "val": "0.0001"},
                             {"key": "noiseMultiplier", "val": "2.0"}, {"key": "l2NormClip", "val": "1.0"},
                             {"key": "secureMode", "val": "true"}, {"key": "alpha", "val": "0.0001"},
                             {"key": "batchSize", "val": 1}, {"key": "maxIter", "val": 5},
                             {"key": "modelName", "val": "横向lr-DPSGD"}, {"key": "modelDesc", "val": "横向lr-DPSGD"}],
         "input": [{"frontComponentId": "15ac0fc2-b40c-4f4e-8d09-8507657ea4c2", "componentCode": "dataSet",
                    "componentName": "选择数据集", "portId": "port2", "pointType": "edge", "pointJson": ""}], "output": []}],
                               "modelPointComponents": [
                                   {"frontComponentId": "d69e97be-0fd1-4b71-ac0b-975f2af1eb79", "shape": "edge",
                                    "input": {"cell": "0770c4ae-c9ba-4e7f-a27e-903fcf3109e5", "port": "port2"},
                                    "output": {"cell": "15ac0fc2-b40c-4f4e-8d09-8507657ea4c2", "port": "port1"}},
                                   {"frontComponentId": "3b09d79d-c562-46de-9098-466f45b6fcd8", "shape": "edge",
                                    "input": {"cell": "15ac0fc2-b40c-4f4e-8d09-8507657ea4c2", "port": "port2"},
                                    "output": {"cell": "381c6a40-c09b-448c-b065-700e0c3886f5", "port": "port1"}}]},
                     "timestamp": timestamp, "nonce": 326, "token": token}

    task_data_id = {"xgb_data": xgb_data, "hlr_data": hlr_data}
    for key in task_data_id:
        resp = requests_handler.visit(
            url=Handler.yaml["host1"] + "/data/model/saveModelAndComponent",
            method="post",
            json=json.loads(json.dumps(task_data_id[key]))
        )
        task_data_id[key] = resp["result"]["modelId"]


    task_id = []
    for key in task_data_id:
        data = '{"modelId":"#modelId#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
        if "#timestamp#" in data:
            data = data.replace("#timestamp#", str(int(time.time())))
        if "#modelId#" in data:
            data = data.replace("#modelId#", str(task_data_id[key]))
        if "#token#" in data:
            data = data.replace("#token#", Handler().token01)
        resp = requests_handler.visit(
            url=Handler.yaml["host1"] + "/data/model/runTaskModel",
            method="get",
            params=json.loads(data)
        )
        print(resp)
        taskId = resp["result"]["taskId"]
        task_id.append(taskId)

    return task_id





if __name__ == "__main__":
    data_path = Handler.conf.DATA_PATH

    #print(runTask_xgb())
    #print(resourceFilePreview01())
    #print(add_resource(host = host3))
    #print(Handler().resourceId03)
    #print(Handler().fileId01)
    # print((Handler().organId01))
    print(runTask())








