class PostgresDetail():

    def __init__(self):
        self.__host = "localhost"
        self.__port = "5432"
        self.__username = "dba"
        self.__password = "123456"

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
