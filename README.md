目录指南：
- data：Excel的测试用例

- reports：测试报告

- testcases：用例方法

- run.py：运行的主程序


需安装以下：
`pip3 install yaml`、`pip3 install pymysql`、`pip3 install openpyxl`
`pip3 install rsa`、`pip3 install requests`、`pip3 install ddt`、`pip3 install unittest`



进入根目录，执行`python run.py`即可

运行结束，可进入<apitest/reports>查看执行生成的测试报告

更改测试环境:
1、进入config目录下
2、修改config.yaml文件中的 host1、host2、host3 对应的测试地址
3、修改 fileId01、fileId02（后续会完善上传文件接口，自动获取fileId）
