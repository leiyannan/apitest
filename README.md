## 目录指南：

### data：Excel的测试用例 及 csv测试数据

### reports：测试报告

### testcases：用例方法

### run.py：运行的主程序


## 操作指南：

### 一、需安装以下： 
#### pip3 install yaml、pip3 install pymysql、pip3 install openpyxl、pip3 install rsa、pip3 install requests、pip3 install requests_toolbelt、pip3 install ddt、pip3 install unittest

### 二、更改测试环境（进入config目录下的config.yaml文件，进行以下操作）:
#### （1）修改host---host1、host2、host3
#### （2）修改数据库连接配置---db
#### （3）修改测试数据---test_data，首先将测试用的csv文件放置data目录下，替换相应任务的测试数据
#### （4）确保host1跟host2、host2已建立连接

### 三、进入根目录，执行python run.py即可

