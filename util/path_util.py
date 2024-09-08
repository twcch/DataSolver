import os


class PathUtil():

    def __init__(self):
        self.__user = os.path.expanduser("~")
        self.__desktop = os.path.join(self.__user, "Desktop")
        self.__downloads = os.path.join(self.__user, "Downloads")
        self.__documents = os.path.join(self.__user, "Documents")

        self.__code_folder = os.path.join(self.__documents, "Code")
        self.__datascience_folder = os.path.join(self.__code_folder , "DataScience")

        self.__keys_folder = os.path.join(self.__datascience_folder, "_keys")

    def get_user(self):
        return self.__user

    def get_desktop(self):
        return self.__desktop

    def get_downloads(self):
        return self.__downloads

    def get_documents(self):
        return self.__documents

    def get_documents_dev(self):
        return self.__documents_dev

    def get_code_folder(self):
        return self.__code_folder

    def get_datascience_folder(self):
        return self.__datascience_folder

    def get_keys_folder(self):
        return self.__keys_folder