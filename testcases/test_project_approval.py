import json
import time
import unittest
import ddt

from common import requests_handler, yaml_handler
from middleware.handler import Handler,getProjectDetails

# 初始化数据
logger = Handler.logger
env_data = Handler()
test_data = Handler.excel.read_data("project_approval")

@ddt.ddt
class TestResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.pjtion01= getProjectDetails()
        cls.pjtion02 = getProjectDetails()
        cls.pjtion03 = getProjectDetails()

    def setUp(self) -> None:
        pass
        #self.db = env_data.db_class()

    def tearDown(self) -> None:
        pass
        #self.db.close()

    @ddt.data(*test_data)
    def test_resource(self,test_info):
        # print(self.organId)
        # print(self.resultId)
        # print(self.pid01)

        data = test_info["data"]
        if "#token#" in data:
            data = data.replace("#token#", env_data.yaml["test"]["token"])
        if "#timestamp#" in data:
            data = data.replace("#timestamp#", str(int(time.time())))
        if "#organId01#" in data:
            data = data.replace("#organId01#", str(self.pjtion01[1]))
        if "#resultId01#" in data:
            data = data.replace("#resultId01#", str(self.pjtion01[0]))
        if "#organId02#" in data:
            data = data.replace("#organId02#", str(self.pjtion02[1]))
        if "#organId03#" in data:
            data = data.replace("#organId03#", str(self.pjtion03[1]))
        if "#resultId03#" in data:
            data = data.replace("#resultId03#", str(self.pjtion03[0]))
        print(data)


        actual = requests_handler.visit(
            url=env_data.yaml["host4"] + test_info["url"],
            method=test_info["method"],
            # headers=json.loads(test_info["header"]),
            data=json.loads(data)
        )
        print(actual)
        expected_dict = eval(test_info["expected"])
        print(expected_dict)
        # # 断言：code和msg
        try:
            for key, value in expected_dict.items():
                self.assertTrue(value == actual[key])
            logger.info("{}：测试用例通过".format(test_info["title"]))
        except AssertionError as e:
            logger.error("{}：测试用例无法通过：{}".format(test_info["title"],e))
            raise e


if __name__ == '__main__':
    unittest.main()
