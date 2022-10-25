# 进行登录+pir+psi+xgb的业务场景性能测试
# -*- coding: UTF-8 -*-
import random
import time
import rsa
import base64
import requests

from locust import HttpUser, task, TaskSet,events


@events.test_start.add_listener
def on_test_start(**kwargs):
    print('===测试最开始提示===')


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print('===测试结束了提示===')

key_str = '''
    -----BEGIN PUBLIC KEY-----
    {}
    -----END PUBLIC KEY-----
'''

class UserBehavior_workflow1(TaskSet):

    # 初始化
    def on_start(self):
        print('这是SETUP，每次实例化User前都会执行！')


    # 登录任务token
    def test_login(self):
        key_url = "http://test1.primihub.com/prod-api/sys/common/getValidatePublicKey?timestamp=" + str(
            int(time.time())) + "&nonce=" + str(random.randint(0, 9))
        result = requests.get(key_url).json()["result"]
        publicKey = result["publicKey"]
        publicKeyName = result["publicKeyName"]
        pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.format(publicKey).encode())
        cryptedMessage = rsa.encrypt("123456".encode(encoding="utf-8"), pubKey)
        key_str_text = base64.b64encode(cryptedMessage)
        data = {
            "userAccount": "test",
            "userPassword": key_str_text,  # key_str_text
            "validateKeyName": publicKeyName,
            "timestamp": str(int(time.time())),
            "nonce": str(random.randint(0, 9))
        }
        # 发送首页请求给服务器 post
        res = requests.post("http://test1.primihub.com/prod-api/sys/user/login", data=data).json()
        token = res["result"]["token"]
        # code = res["code"]
        # assert res.code == 0
        # print("code返回:"+ code +"登录测试成功")
        loc = res["code"]
        if loc == 0:
            print("登录测试成功")
        else:
            print("登录测试失败")
        return token

    # 登录任务token
    # @task(2)
    # def login(self):
    #     self.test_login()


    # pir任务
    # @task(4)
    # def pir(self):
    #     token = self.test_login()
    #     pir_url = "/data/pir/pirSubmitTask"
    #     data = {
    #         "serverAddress":'http://fusion.primihub.svc.cluster.local:8080/',
    #         "resourceId": "2b598a7e3298-d77e0b68-a33f-4bc3-bb57-8839be0a4ec1",
    #         "pirParam": '123,234,345',
    #         "timestamp": str(int(time.time())),
    #         "nonce": str(random.randint(0, 9)),
    #         "token": token
    #     }
    #
    #     res = self.client.get(pir_url, params=data).json()
    #     loc = res["code"]
    #     if loc == 0:
    #         print("pir返回成功")
    #     else:
    #         print("pir返回失败")

    # # psi任务
    # @task(4)
    # def psi(self):
    #     # 构造测试数据
    #     token = self.test_login()
    #     psi_url = "/data/psi/saveDataPsi"
    #     data = {
    #         "ownOrganId": "8bf56ee6-b004-4ada-b078-591acb22b324",
    #         "ownResourceId": 60,
    #         "ownKeyword": "guaranteetype",
    #         "otherOrganId": "2cad8338-2e8c-4768-904d-2b598a7e3298",
    #         "otherResourceId": "2b598a7e3298-a56a37fa-0456-400e-bd5d-3a1390418b0c",
    #         "otherKeyword": "guaranteetype",
    #         "outputFormat": "0",
    #         "outputFilePathType": "0",
    #         "outputContent": "0",
    #         "resultOrgan[0]": "8bf56ee6-b004-4ada-b078-591acb22b324",
    #         "resultOrganIds": "8bf56ee6-b004-4ada-b078-591acb22b324",
    #         "outputNoRepeat": "0",
    #         "resultName": "testpsi-testpsi",
    #         "remarks": '描述',
    #         "serverAddress": "http://fusion.primihub.svc.cluster.local:8080/",
    #         "psiTag":'0',
    #         "ownOrganName": "test1",
    #         "otherOrganName": "test2",
    #         "timestamp": str(int(time.time())),
    #         "nonce": str(random.randint(0, 9)),
    #         "token": token
    #     }
    #     # assert isinstance(self.client.get(psi_url, data).json, object)
    #     res = self.client.post(psi_url, data).json()
    #     loc = res["code"]
    #     if loc == 0:
    #         print("psi返回成功")
    #     else:
    #         print("psi返回失败")

    # tasks = {test_login: 2, test_search: 3, test_reg: 1}

    # mid任务
    @task(4)
    def mid(self):
        token = self.test_login()
        data = {
            "taskId": 109,
            "timestamp": str(int(time.time())),
            "nonce": str(random.randint(0, 9)),
            "token": token
        }
        mid_url = "/data/model/restartTaskModel"
        res = self.client.get(mid_url, params=data).json()
        loc = res["code"]
        if loc == 0:
            print("模型返回成功")
        else:
            print("模型返回失败")



class WebSiteUser(HttpUser):
    host = "http://test1.primihub.com/prod-api"
    tasks = [UserBehavior_workflow1]
    min_wait = 2000
    max_wait = 5000