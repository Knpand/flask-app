import mysql.connector as mysql
import sqlalchemy as db
import datetime

# *****************
# 初期設定
# *****************
dt_now = datetime.datetime.now()
user_name = "light"
password = "light"
host = "db"  # docker-composeで定義したMySQLのサービス名
database_name = "db"

conn = mysql.connect(
    host="db",
    user="light",
    passwd="light",
    port=3306,
    database="db",
    buffered = True
)

class SQLhandler:
    def select_all(self):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        sql = "select * from students"
        # sql = "insert into books values (NULL, "
        cur.execute(sql)
        data = cur.fetchall()
        return data