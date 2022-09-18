"""收集用例、运行用例、生成测试报告的主程序"""
import unittest
import os
from datetime import datetime
from config import config
from libs.HTMLTestRunnerNew import HTMLTestRunner

# 加载用例
loader = unittest.TestLoader()
suits = loader.discover(config.CASE_PATH)

# 测试报告的路径
ts = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
reports_filename = 'reports-{}.html'.format(ts)
reports_path = os.path.join(config.REPORTS_PATH,reports_filename)

# HTML 测试报告，模板,需导入
with open(reports_path, 'wb') as f:
    runner = HTMLTestRunner(
        f,
        title='primihub管理平台测试报告',
        description='测试报告描述',
        tester='lyn'
    )
    runner.run(suits)

