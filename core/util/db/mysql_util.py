from sqlalchemy import create_engine
from mysql.connector import Error
import mysql.connector
import pandas as pd


class MysqlUtil():

    def __init__(self,
                 database,
                 host="localhost",
                 port="3306",
                 username="dba",
                 password="123456"):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__database = database

        self.__database_url = f"mysql+pymysql://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__database}"
        self.__engine = create_engine(self.__database_url)

        self.__connection = mysql.connector.connect(
            host=self.__host,
            port=self.__port,
            user=self.__username,
            password=self.__password,
            database=self.__database
        )

        self.__cursor = self.__connection.cursor()

    def dataframe_to_mysql(self, table_name, dataframe, if_exists="replace", index=False):
        dataframe.to_sql(table_name, self.__engine, if_exists=if_exists, index=index)

    def dataframe_from_mysql(self, table_name):
        dataframe = pd.read_sql(table_name, self.__engine)
        return dataframe

    def execute_query(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def close(self):
        self.__cursor.close()
        self.__connection.close()

    def close_cursor(self):
        self.__cursor.close()

    def close_connection(self):
        self.__connection.close()

    def get_host(self):
        return self.__host

    def set_host(self, host):
        self.__host = host

    def get_port(self):
        return self.__port

    def set_port(self, port):
        self.__port = port

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_database(self):
        return self.__database

    def set_database(self, database):
        self.__database = database

    def get_database_url(self):
        return self.__database_url

    def set_database_url(self, database_url):
        self.__database_url = database_url

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine
