
import json
import os

import time

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
    def resourceId01(self):
        # test1本地资源ID
        return add_resource01()["resourceId01"]

    @property
    def resourceFusionId01(self):
        # test1联邦资源ID
        return add_resource01()["resourceFusionId01"]

    @property
    def fieldList(self):
        # test1本地资源
        return getdataresource()

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
        return add_project()[0]

    @property
    def pid01(self):
        # test1本地项目id
        return add_project()[1]

    @property
    def pid02(self):
        # test1本地项目id
        return getprojectlist()[1]

    @property
    def resultId(self):
        # test1本地项目id
        return getProjectDetails()[0]

    @property
    def organId01(self):
        # test1机构id
        return getLocalOrganInfo()[0]

    @property
    def organName01(self):
        # test1机构名称
        return getLocalOrganInfo()[1]

    @property
    def socketserver(self):
        # test1中心节点
        return getLocalOrganInfo()[2]

    @property
    def organId02(self):
        # test1机构id
        return getLocalOrganInfo()[3]

    @property
    def organName02(self):
        # test1机构名称
        return getLocalOrganInfo()[4]

    @property
    def organId03(self):
        # test1机构id
        return getLocalOrganInfo()[5]

    @property
    def organName03(self):
        # test1机构名称
        return getLocalOrganInfo()[6]


def getLocalOrganInfo():
    #获取当前环境的机构ID级中心节点地址
    data = '{"timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    resp01 = requests_handler.visit(
        url=Handler.yaml["host1"] + "/sys/organ/getLocalOrganInfo",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    organId01 = resp01["result"]["sysLocalOrganInfo"]["organId"]
    organName01 = resp01["result"]["sysLocalOrganInfo"]["organName"]
    socketserver = resp01["result"]["sysLocalOrganInfo"]["fusionList"][0]["serverAddress"]

    resp02 = requests_handler.visit(
        url=Handler.yaml["host2"] + "/sys/organ/getLocalOrganInfo",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    organId02 = resp02["result"]["sysLocalOrganInfo"]["organId"]
    organName02 = resp02["result"]["sysLocalOrganInfo"]["organName"]

    resp03 = requests_handler.visit(
        url=Handler.yaml["host3"] + "/sys/organ/getLocalOrganInfo",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    organId03 = resp03["result"]["sysLocalOrganInfo"]["organId"]
    organName03 = resp03["result"]["sysLocalOrganInfo"]["organName"]

    return organId01,organName01,socketserver,organId02,organName02,organId03,organName03

def add_resource01():
    # test1环境添加资源
    data:str = '{"resourceName":"#resourceName#","resourceDesc":"55555","tags":["555"],"resourceSource":1,"resourceAuthType":1,"fileId":"#fileId01#","fieldList":[{"fieldId":null,"fieldName":"Class","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"y","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x1","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x2","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x3","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x4","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x5","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0}],"fusionOrganList":[],"timestamp":"#timestamp#","nonce":691,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#fileId01#" in data:
        data = data.replace("#fileId01#", Handler().yaml["test"]["fileId01"])
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#resourceName#" in data:
        data = data.replace("#resourceName#", Handler().yaml["test_name"]["resourceName01"])

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

def getdataresource():

    data = '{"resourceId":"#resourceId#","timestamp":"#timestamp#","nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#resourceId#" in data:
        data = data.replace("#resourceId#", str(Handler().resourceId01))
    resp = requests_handler.visit(
        url=Handler.yaml["host1"] + "/data/resource/getdataresource",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    fieldList = resp["result"]["fieldList"]
    for line in fieldList:
        del line["createDate"]
        del line["fieldAs"]
    fieldList = str(fieldList).replace("'", '"').replace("False", "0").replace("None", "null").replace(" ", "")
    return fieldList


def add_resource02():
    # test2环境添加资源
    data:str = '{"resourceName":"#resourceName#","resourceDesc":"资源描述","tags":["test"],"resourceSource":1,"resourceAuthType":1,"fileId":"#fileId02#","fieldList":[{"fieldId":null,"fieldName":"x6","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x7","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x8","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x9","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x10","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x11","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0},{"fieldId":null,"fieldName":"x12","fieldType":"integer","fieldDesc":null,"relevance":0,"grouping":0,"protectionStatus":0}],"fusionOrganList":[],"timestamp":"#timestamp#","nonce":212,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#fileId02#" in data:
        data = data.replace("#fileId02#", Handler().yaml["test"]["fileId02"])
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#resourceName#" in data:
        data = data.replace("#resourceName#", Handler().yaml["test_name"]["resourceName02"])

    resp = requests_handler.visit(
        url=Handler.yaml["host2"] + "/data/resource/saveorupdateresource",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )
    resourceId02 = resp["result"]["resourceId"]
    resourceFusionId02 = resp["result"]["resourceFusionId"]
    print(resourceFusionId02)
    return {"resourceId02":resourceId02,"resourceFusionId02":resourceFusionId02}

def add_project():
    # 使用test1和test2的新增资源，在test1环境新建项目
    data:str = '{"serverAddress":"#serverAddress#","projectName":"#projectName01#","projectDesc":"new_project","projectOrgans":[{"organId":"#organId02#","participationIdentity":2,"resourceIds":["#resourceFusionId02#"]},{"organId":"#organId01#","participationIdentity":1,"resourceIds":["#resourceFusionId01#"]}],"timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    if "#serverAddress#" in data:
        data = data.replace("#serverAddress#", str(Handler().socketserver))
    if "#projectName01#" in data:
        data = data.replace("#projectName01#", Handler().yaml["test_name"]["projectName01"])
    if "#organId01#" in data:
        data = data.replace("#organId01#", str(Handler().organId01))
    if "#organId02#" in data:
        data = data.replace("#organId02#", str(Handler().organId02))
    if "#resourceFusionId01#" in data:
        data = data.replace("#resourceFusionId01#", str(Handler().resourceFusionId01))
    if "#resourceFusionId02#" in data:
        data = data.replace("#resourceFusionId02#", str(Handler().resourceFusionId02))
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    print(data)
    resp = requests_handler.visit(
        url=Handler.yaml["host1"] + "/data/project/saveOrUpdateProject",
        method="post",
        # headers=json.loads(test_info["header"]),
        json=json.loads(data)
    )

    projectId = resp['result']['projectId']
    pid01 = resp['result']['id']
    return projectId,pid01

def getprojectlist():
    # test2请求项目列表，获得第一条项目的本地ID，以便进行项目详情接口请求
    projectId,pid01 = add_project()
    data = '{"pageNo":1,"pageSize":10,"timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    print(data)

    resp = requests_handler.visit(
        url=Handler.yaml["host2"] + "/data/project/getProjectList",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    list = resp["result"]["data"]
    projectid02 = []
    for dict in list:
        projectid02.append(dict["projectId"])
    pid_key = projectid02.index(str(projectId))
    pid02 = list[pid_key]["id"]

    return pid01,pid02

def getProjectDetails():
    pid01,pid02 = getprojectlist()
    # test2请求项目详情，获得项目资源真实ID，以便进行项目审核、资源审核
    data = '{"id":"#pid02#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#pid02#" in data:
        data = data.replace("#pid02#", str(pid02))
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])

    resp = requests_handler.visit(
        url=Handler.yaml["host2"] + "/data/project/getProjectDetails",
        method="get",
        # headers=json.loads(test_info["header"]),
        params=json.loads(data)
    )
    #
    resultId = resp["result"]["organs"][1]["resources"][0]["id"]
    organId = resp["result"]["organs"][1]["id"]
    return resultId,organId,pid01

def Projectapproval():
    resultId,organId,pid01 = getProjectDetails()
    data = '{"type":"#type#","id":"#id#","auditStatus":1,"auditOpinion":"审核项目&资源","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])

    projectdata = data.replace("#type#", str(1))
    projectdata = projectdata.replace("#id#", str(organId))
    resourcedata = data.replace("#type#", str(2))
    resourcedata = resourcedata.replace("#id#", str(resultId))

    resp01 = requests_handler.visit(
        url=Handler.yaml["host2"] + "/data/project/approval",
        method="post",
        data=json.loads(projectdata)
    )
    resp02 = requests_handler.visit(
        url=Handler.yaml["host2"] + "/data/project/approval",
        method="post",
        data=json.loads(resourcedata)
    )

    return resp02,pid01

def saveModelAndComponent():
    projectId = Projectapproval()[1]
    data = '{"param":{"projectId":"#projectId#","isDraft":0,"modelComponents":[{"frontComponentId":"cdb278c3-8165-4522-bc50-d5caf13e4061","coordinateX":123.5,"coordinateY":100,"width":120,"height":40,"shape":"start-node","componentCode":"start","componentName":"开始","componentValues":[{"key":"taskName","val":""},{"key":"taskDesc","val":""}],"input":[],"output":[]}],"modelPointComponents":[]},"timestamp":#timestamp#,"nonce":377,"token":"#token#"}'
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#projectId#" in data:
        data = data.replace("#projectId#", str(projectId))
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])

    resp = requests_handler.visit(
        url=Handler.yaml["host1"] + "/data/model/saveModelAndComponent",
        method="post",
        json=json.loads(data)
    )
    modelId = resp["result"]["modelId"]

    requests_data = '{"projectId":"#projectId#","organId":"#organId#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#timestamp#" in requests_data:
        requests_data = requests_data.replace("#timestamp#", str(int(time.time())))
    if "#projectId#" in requests_data:
        requests_data = requests_data.replace("#projectId#", str(projectId))
    if "#token#" in requests_data:
        requests_data = requests_data.replace("#token#", Handler().yaml["test"]["token"])

    requests_data01 = requests_data.replace("#organId#", str(Handler().organId01))
    requests_data02 = requests_data.replace("#organId#", str(Handler().organId02))

    resourceId01 = requests_handler.visit(
        url = Handler.yaml["host1"] + "/data/project/getProjectResourceData",
        method="get",
        params=json.loads(requests_data01)
    )["result"][0]["resourceId"]

    resourceId02 = requests_handler.visit(
        url = Handler.yaml["host1"] + "/data/project/getProjectResourceData",
        method="get",
        params=json.loads(requests_data02)
    )["result"][0]["resourceId"]

    data02 = {"param": {"projectId": str(projectId), "modelId": str(modelId), "isDraft": 1, "modelComponents": [
        {"frontComponentId": "495a09b3-4744-4058-9688-6772e5791de4", "coordinateX": 140.5, "coordinateY": 100,
         "width": 120, "height": 40, "shape": "start-node", "componentCode": "start", "componentName": "开始",
         "componentValues": [{"key": "taskName", "val": "纵向xgb任务"}, {"key": "taskDesc", "val": "纵向xgb任务描述"}],
         "input": [], "output": [
            {"frontComponentId": "0b838296-d584-48c2-acd0-9702eec0562e", "componentCode": "dataSet",
             "componentName": "选择数据集", "portId": "port1", "pointType": "edge", "pointJson": ""}]},
        {"frontComponentId": "0b838296-d584-48c2-acd0-9702eec0562e", "coordinateX": 170, "coordinateY": 260,
         "width": 180, "height": 50, "shape": "dag-node", "componentCode": "dataSet", "componentName": "选择数据集",
         "componentValues": [{"key": "selectData",
                              "val": "[{\"organId\":\"#organId01#\",\"organName\":\"PrimiHub01\",\"resourceId\":\"#resourceId01#\",\"resourceName\":\"#resourceName01#\",\"resourceRowsCount\":50,\"resourceColumnCount\":7,\"resourceContainsY\":1,\"auditStatus\":1,\"participationIdentity\":1,\"fileHandleField\":[\"Class\",\"y\",\"x1\",\"x2\",\"x3\",\"x4\",\"x5\"],\"calculationField\":\"Class\"},{\"organId\":\"#organId02#\",\"organName\":\"PrimiHub02\",\"resourceId\":\"#resourceId02#\",\"resourceName\":\"#resourceName02#\",\"resourceRowsCount\":50,\"resourceColumnCount\":7,\"resourceContainsY\":0,\"auditStatus\":1,\"participationIdentity\":2,\"fileHandleField\":[\"x6\",\"x7\",\"x8\",\"x9\",\"x10\",\"x11\",\"x12\"],\"calculationField\":\"x6\"}]"}],
         "input": [{"frontComponentId": "495a09b3-4744-4058-9688-6772e5791de4", "componentCode": "start",
                    "componentName": "开始", "portId": "port2", "pointType": "edge", "pointJson": ""}], "output": [
            {"frontComponentId": "38d66ca5-e0aa-436d-af0f-94a5f469eb21", "componentCode": "model",
             "componentName": "模型选择", "portId": "port1", "pointType": "edge", "pointJson": ""}]},
        {"frontComponentId": "38d66ca5-e0aa-436d-af0f-94a5f469eb21", "coordinateX": 60, "coordinateY": 420,
         "width": 180, "height": 50, "shape": "dag-node", "componentCode": "model", "componentName": "模型选择",
         "componentValues": [{"key": "modelType", "val": "2"}, {"key": "modelName", "val": "纵向xgb模型"},
                             {"key": "modelDesc", "val": "纵向xgb模型描述"}, {"key": "arbiterOrgan", "val": ""}], "input": [
            {"frontComponentId": "0b838296-d584-48c2-acd0-9702eec0562e", "componentCode": "dataSet",
             "componentName": "选择数据集", "portId": "port2", "pointType": "edge", "pointJson": ""}], "output": []}],
                        "modelPointComponents": [
                            {"frontComponentId": "1148b089-b45f-4d53-bdc3-bfd0c02f8b4e", "shape": "edge",
                             "input": {"cell": "495a09b3-4744-4058-9688-6772e5791de4", "port": "port2"},
                             "output": {"cell": "0b838296-d584-48c2-acd0-9702eec0562e", "port": "port1"}},
                            {"frontComponentId": "1e0604de-73cc-4a27-b05f-2c8acdca7cc2", "shape": "edge",
                             "input": {"cell": "0b838296-d584-48c2-acd0-9702eec0562e", "port": "port2"},
                             "output": {"cell": "38d66ca5-e0aa-436d-af0f-94a5f469eb21", "port": "port1"}}]},
              "timestamp": str(int(time.time())), "nonce": 853, "token": Handler().yaml["test"]["token"]}

    data02 = json.dumps(data02)

    if "#organId01#" in data02:
        data02 = data02.replace("#organId01#", str(Handler().organId01))
    if "#resourceId01#" in data02:
        data02 = data02.replace("#resourceId01#", resourceId01)
    if "#resourceName01#" in data02:
        data02 = data02.replace("#resourceName01#", Handler().yaml["test_name"]["resourceName01"])
    if "#organId02#" in data02:
        data02 = data02.replace("#organId02#", str(Handler().organId02))
    if "#resourceId02#" in data02:
        data02 = data02.replace("#resourceId02#", resourceId02)
    if "#resourceName02#" in data02:
        data02 = data02.replace("#resourceName02#", Handler().yaml["test_name"]["resourceName02"])
    print(data02)


    resp = requests_handler.visit(
        url=Handler.yaml["host1"] + "/data/model/saveModelAndComponent",
        method="post",
        json=json.loads(data02)
    )
    modelId = resp["result"]["modelId"]

    return modelId

def runTask_xgb():
    modelId = saveModelAndComponent()
    data = '{"modelId":"#modelId#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
    if "#timestamp#" in data:
        data = data.replace("#timestamp#", str(int(time.time())))
    if "#modelId#" in data:
        data = data.replace("#modelId#", str(modelId))
    if "#token#" in data:
        data = data.replace("#token#", Handler().yaml["test"]["token"])
    resp = requests_handler.visit(
        url=Handler.yaml["host1"] + "/data/model/runTaskModel",
        method="get",
        params=json.loads(data)
    )
    xgb_taskId = resp["result"]["taskId"]

    return xgb_taskId





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

    #print(getLocalOrganInfo())
    # print(Handler().organId01)
    # print(Handler().organId02)
    # print(Handler().organId03)
    # print(Handler().socketserver)
    #print(add_resource01())
    #print(add_resource02())
    #print(add_project())
    #print(getprojectlist())
    #print(getProjectDetails())
    #print(Projectapproval())
    #print(saveModelAndComponent())
    print(runTask_xgb())
    #print(getdataresource())
    #print(Handler().fieldList)
    #print(getLocalOrganInfo())







