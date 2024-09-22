import random
import pandas as pd
from datetime import datetime

from backup.core.util.path_util import PathUtil


class FileUtil():

    def __init__(self):
        self.__path_util = PathUtil()
        self.__file_folder = self.__path_util.get_temp_data_folder()

    def generate_temp_file(self, dataframe: pd.DataFrame) -> str:
        current_timestamp = int(datetime.now().timestamp())
        random_number = random.randint(1000, 9999)

        file_path = self.__file_folder + "/TEMP_FILE" + str(current_timestamp) + str(random_number) + ".csv"

        dataframe.to_csv(file_path, index=False)

        return file_path

    def generate_temp_file_for_name(self, dataframe: pd.DataFrame, name: str) -> str:
        file_path = self.__file_folder + "/" + name + ".csv"

        dataframe.to_csv(file_path, index=False)

        return file_path
