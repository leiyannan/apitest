import json
import time
import unittest
import ddt

from common import requests_handler, yaml_handler
from middleware.handler import Handler

# 初始化数据
logger = Handler.logger
env_data = Handler()
test_data = Handler.excel.read_data("resource")

@ddt.ddt
class TestResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # cls.token = yaml["test"]["token"]
        # cls.userid = yaml["test"]["userid"]
        cls.resourceId = env_data.resourceId01

    def setUp(self) -> None:
        self.db = env_data.db_class()

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_resource(self,test_info):

        data = test_info["data"]
        if "#token#" in data:
            data = data.replace("#token#",env_data.yaml["test"]["token"])

        if "#timestamp#" in data:
            data = data.replace("#timestamp#",str(int(time.time())))

        if "#resourceId#" in data:
            data = data.replace("#resourceId#", str(self.resourceId))

        # if test_info["sql_code"]:
        #     before_resource = self.db.query(
        #         "select * from privacy_test1.data_resource where user_id={}".format(self.userid),
        #         one=False
        #     )
        #     print(len(before_resource))


        actual = requests_handler.visit(
            url=env_data.yaml["host2"] + test_info["url"],
            method=test_info["method"],
            #headers=json.loads(test_info["header"]),
            json=json.loads(data)
        )
        print(actual)
        expected_dict = eval(test_info["expected"])
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
