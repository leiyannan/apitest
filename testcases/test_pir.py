import json
import time
import unittest
import ddt

from common import requests_handler, yaml_handler
from middleware.handler import Handler

# 初始化数据
logger = Handler.logger
env_data = Handler()
test_data = Handler.excel.read_data("pir")

@ddt.ddt
class TestResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.resourceId = env_data.pir_data_FusionId
        cls.token = env_data.token01


    def setUp(self) -> None:
        pass
        #self.db = env_data.db_class()

    def tearDown(self) -> None:
        pass
        #self.db.close()


    @ddt.data(*test_data)
    def test_resource(self,test_info):

        data = test_info["data"]

        if "#resourceId#" in data:
            data = data.replace("#resourceId#", str(self.resourceId))
        if "#timestamp#" in data:
            data = data.replace("#timestamp#", str(int(time.time())))
        if "#token#" in data:
            data = data.replace("#token#", self.token)

        #data = json.dumps(data)
        #data = json.loads(json.dumps(data))

        print(data)



        actual = requests_handler.visit(
            url=env_data.yaml["host1"] + test_info["url"],
            method=test_info["method"],
            params=json.loads(data)
        )
        print(actual)
        expected_dict = eval(test_info["expected"])
        print(expected_dict)
        # 断言：code和msg
        try:
            for key, value in expected_dict.items():
                self.assertTrue(value == actual[key])
            logger.info("{}：测试用例通过".format(test_info["title"]))
        except AssertionError as e:
            logger.error("{}：测试用例无法通过：{}".format(test_info["title"],e))
            raise e


if __name__ == '__main__':
    unittest.main()
