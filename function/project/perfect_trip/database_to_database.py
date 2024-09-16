import pandas as pd

from core.util.db.mysql_util import MysqlUtil

mysql_util_1 = MysqlUtil(database="perfect_trip_db",
                         host="iorlvm.i234.me",
                         port="8995",
                         username="tia201group1",
                         password="1puorg102ait")

mysql_util_2 = MysqlUtil(database="backup_perfect_trip_db")

table_name = mysql_util_1.execute_query("SHOW TABLES")
table_number = len(table_name)

for i in range(table_number):
    tn = table_name[i][0]
    if tn != "images":
        l = mysql_util_1.dataframe_from_mysql(f"SELECT * FROM {tn}")
        df = pd.DataFrame(l)
        mysql_util_2.dataframe_to_mysql(tn, df)
