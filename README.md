目录指南：

data：Excel的测试用例 及 csv测试数据

reports：测试报告

testcases：用例方法

run.py：运行的主程序

需安装以下： pip3 install yaml、pip3 install pymysql、pip3 install openpyxl pip3 install rsa、pip3 install requests、pip3 install ddt、pip3 install unittest

进入根目录，执行python run.py即可

运行结束，可进入<apitest/reports>查看执行生成的测试报告

更改测试环境: 
一：进入config目录下的config.yaml文件，进行一下操作：
（1）修改host（ host1、host2、host3 ）对应的测试地址
（2）修改数据库连接配置
（3）若要更换测试数据集，首先将csv文件放置data目录下，将csv文件名在config.yaml文件中替换