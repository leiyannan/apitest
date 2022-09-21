import json
import time
import unittest
import ddt


from common import requests_handler
from middleware.handler import Handler,add_project,MysqlHandlerMid

logger = Handler.logger
env_data = Handler()
# test_data = Handler.excel.read_data("protect")

# @ddt.ddt
class TestProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.token = env_data.token_test1

    def setUp(self) -> None:
        self.db = MysqlHandlerMid()
        self.pid = env_data.pid

    def tearDown(self) -> None:
        self.db.close()

    # @ddt.data(*test_data)
    def test_project(self):
        data= {
            "id":int(self.pid),
            "timestamp":1663432979839,
            "nonce":622,
            "token":self.token
        }
        # test1禁用/启用项目
        res = requests_handler.visit(
            url=env_data.yaml["host2"]+"/project/closeProject",
            method="post",
            data=data
        )
        self.assertTrue(res["code"]==0)

if __name__ == '__main__':
    unittest.main()

