import json
import time
import unittest
import ddt

from common import requests_handler, yaml_handler
from middleware.handler import Handler, getModel_vel

# 初始化数据
logger = Handler.logger
env_data = Handler()
test_data = Handler.excel.read_data("task_save_run")


@ddt.ddt
class TestResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.getModel_vel = getModel_vel()
        cls.token = env_data.token01

    def setUp(self) -> None:
        pass
        # self.db = env_data.db_class()

    def tearDown(self) -> None:
        pass
        # self.db.close()

    @ddt.data(*test_data)
    def test_resource(self, test_info):

        data: str = test_info["data"]
        if "#token#" in data:
            data = data.replace("#token#", self.token)
        if "#timestamp#" in data:
            data = data.replace("#timestamp#", str(int(time.time())))
        if "#projectId#" in data:
            data = data.replace("#projectId#", str(self.getModel_vel["projectId"]))
        if "#xgb_val#" in data:
            data = data.replace("#xgb_val#", json.dumps(json.dumps(self.getModel_vel["xgb_val"])))
        if "#hlr_val#" in data:
            data = data.replace("#hlr_val#", json.dumps(json.dumps(self.getModel_vel["hlr_val"])))
        if "#lrnn_val#" in data:
            data = data.replace("#lrnn_val#", json.dumps(json.dumps(self.getModel_vel["lrnn_val"])))
        if "#mpclr_val#" in data:
            data = data.replace("#mpclr_val#", json.dumps(json.dumps(self.getModel_vel["mpclr_val"])))


        actual = requests_handler.visit(
            url=env_data.yaml["host1"] + test_info["url"],
            method=test_info["method"],
            # headers=json.loads(test_info["header"]),
            json =json.loads(data)
        )
        #print(actual)

        # 获取modleId,发起任务运行
        modelId = actual["result"]["modelId"]
        rundata = '{"modelId":"#modelId#","timestamp":#timestamp#,"nonce":622,"token":"#token#"}'
        if "#timestamp#" in rundata:
            rundata = rundata.replace("#timestamp#", str(int(time.time())))
        if "#modelId#" in rundata:
            rundata = rundata.replace("#modelId#", str(modelId))
        if "#token#" in rundata:
            rundata = rundata.replace("#token#", self.token)

        resp = requests_handler.visit(
            url=Handler.yaml["host1"] + "/data/model/runTaskModel",
            method="get",
            params=json.loads(rundata)
        )
        print(resp)

        expected_dict = eval(test_info["expected"])
        print(expected_dict)
        # 断言：code和msg
        try:
            for key, value in expected_dict.items():
                self.assertTrue(value == actual[key])
            logger.info("{}：测试用例通过".format(test_info["title"]))
        except AssertionError as e:
            logger.error("{}：测试用例无法通过：{}".format(test_info["title"], e))
            raise e


if __name__ == '__main__':
    unittest.main()
