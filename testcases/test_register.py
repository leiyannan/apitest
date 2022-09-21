import random
import time
import unittest
import ddt

from common import requests_handler
from middleware.handler import Handler,MysqlHandlerMid

# 初始化数据
logger = Handler.logger
test_data = Handler.excel.read_data("register")

@ddt.ddt
class TestRegister(unittest.TestCase):

    @ddt.data(*test_data)
    def test_register(self,test_info):
        # 判断测试用例数据有没有#phone#，如果有，就要替换成动态生成的手机号码
        if "#phone" in test_info["data"]:
            phone = self.random_phone()
            test_info["data"] = test_info['data'].replace("#phone#",phone)

        data = eval(test_info["data"])
        # print(data)
        # data.update(Handler.add_params)
        data["timestamp"] = str(int(time.time()))
        data["nonce"] = str(random.randint(0, 9))
        # 访问接口
        actual = requests_handler.visit(
            url=test_info["url"],
            method=test_info["method"],
            data=data,
        )
        print(actual)

        expected_dict = eval(test_info["expected"])

        # 断言：code和msg
        try:
            for key, value in expected_dict.items():
                self.assertTrue(value == actual[key])

            if actual["code"] == 0:
                # 如果注册成功，数据库当代中需要有这个手机号码的记录
                db = MysqlHandlerMid()
                # 查询数据库当中有没有插入账号注册成功的记录
                sql_code = "select * from privacy_test1.sys_user where user_account={};".format(data["userAccount"])
                user = db.query(sql_code)
                    # 测试通过
                self.assertTrue(user)

            logger.info("{}：测试用例通过".format(test_info["title"]))
        except AssertionError as e:
            logger.error("{}：测试用例无法通过：{}".format(test_info["title"],e))
            raise e

            # if actual["code"] == 0:
            #     # 如果注册成功，数据库当代中需要有这个手机号码的记录
            #     db = MysqlHandlerMid()
            #     # 查询数据库当中有没有插入账号注册成功的记录
            #     sql_code = "select * from privacy_test1.sys_user where user_account={};".format(data["userAccount"])
            #     user = db.query(sql_code)
            #         # 测试通过
            #     self.assertTrue(user)


    def random_phone(self):
        """随机生成一个动态的手机号码
        注册成功的用例当中，需要一个没有被注册过的手机号，需要查询数据库
        """
        # 第一步：随机生成一个手机号
        while True:
            phone = "13"
            for i in range(9):
                num = random.randint(0, 9)
                phone += str(num)
            print(phone)
            # 第二部：查询数据库，如果数据库当中有这个手机号，则再次生成；若无，则返回该手机号；while
            db = MysqlHandlerMid()
            sql_code = "select * from privacy_test1.sys_user where user_account={};".format(phone)
            phone_record = db.query(sql_code)
            if not phone_record:
                db.close()
                return phone
            db.close()


if __name__ == '__main__':
    unittest.main()






