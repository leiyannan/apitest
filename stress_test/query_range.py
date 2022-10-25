# 进行接口性能测试
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


class UserBehavior_workflow1(TaskSet):

    # 初始化
    def on_start(self):
        print('这是SETUP，每次实例化User前都会执行！')

    # 日志
    @task(4)
    def query_range(self):
       # token = "SU202210240228069E60976B75557E1C6A260266E234B512"
        data = {
            "query": '{container ="node0"}',
            "start": 1666270638,
        }
        mid_url = "/loki/api/v1/query_range"
        res = self.client.get(mid_url, params=data).json()
        loc = res["status"]
        if loc == "success":
            print("日志返回成功")
        else:
            print("日志返回失败")


class WebSiteUser(HttpUser):
    host = "http://118.190.39.100:30005"
    tasks = [UserBehavior_workflow1]
    min_wait = 2000
    max_wait = 5000