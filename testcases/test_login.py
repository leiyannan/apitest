# -*- coding: UTF-8 -*-
import random
import time
import rsa
import base64
import requests
import unittest
import ddt

from common import requests_handler
from middleware.handler import Handler


# 初始化数据
logger = Handler.logger
test_data = Handler.excel.read_data("login")


key_str = '''
    -----BEGIN PUBLIC KEY-----
    {}
    -----END PUBLIC KEY-----
'''

@ddt.ddt
class TestLogin(unittest.TestCase):

    def getkey(self):
        key_url = "http://test1.primihub.com/prod-api/sys/common/getValidatePublicKey?timestamp=" + str(
            int(time.time())) + "&nonce=" + str(random.randint(0, 9))
        result = requests.get(key_url).json()["result"]
        publicKey = result["publicKey"]
        publicKeyName = result["publicKeyName"]
        return publicKeyName, publicKey

    @ddt.data(*test_data)
    def test_login(self,test_info):
        publicKeyName, publicKey = self.getkey()

        # 原来Excel中的data数据
        data = eval(test_info['data'])
        # 密码加密
        pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(key_str.format(publicKey).encode())
        passwd = data['userPassword']
        cryptedMessage = rsa.encrypt(passwd.encode(encoding="utf-8"), pubKey)
        key_str_text = base64.b64encode(cryptedMessage)

        # 修改密码
        data['userPassword'] = key_str_text
        # 增加字典键值，得到最终的data
        data['validateKeyName'] = publicKeyName
        # data.update(Handler.add_params)
        data["timestamp"] = str(int(time.time()))
        data["nonce"] = str(random.randint(0, 9))

        # 访问接口，获取实际结果
        actual = requests_handler.visit(
             url = test_info['url'],
             method = test_info['method'],
             data = data
        )
        print(actual)
        # 预期结果
        expected_dict = eval(test_info['expected'])

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
