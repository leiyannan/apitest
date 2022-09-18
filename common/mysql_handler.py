import pymysql
from pymysql.cursors import DictCursor

class MysqlHandler():
    def __init__(
            self,
            host=None,
            port=None,
            user=None,
            password=None,
            charset="utf8",
            cursorclass=DictCursor
    ):
        self.conn = pymysql.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            charset = charset,
            cursorclass = cursorclass
        )
        self.cursor = self.conn.cursor()

    def query(self,sql, one=True):
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()


    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = MysqlHandler(
        host="118.190.39.100",
        port=27936,
        user="primihub",
        password="primihub@123",
        charset="utf8",
        cursorclass=DictCursor
    )
    data = db.query("SELECT * FROM privacy_test1.sys_user WHERE user_account={} LIMIT 10;".format(13699223155))
    print(data)
