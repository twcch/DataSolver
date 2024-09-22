from backup.function.api_data_processor.api_data_processor import ApiDataProcessor
from backup.core.util.key_util import KeyUtil
from backup.function.api_data_processor.constant.data_table import DataTable
import tejapi
import pandas as pd


class TejDataProcessor(ApiDataProcessor):
    def __init__(self):
        self.__api_key = KeyUtil().get_tej_api_key()
        tejapi.ApiConfig.api_key = self.__api_key

    def get_data(self, table=[], src="", desc="") -> pd.DataFrame:
        if len(table) == 0:
            tables = DataTable.tej_test_table_dict
            for i in range(len(tables)):
                data = pd.DataFrame(tejapi.get(tables))
                data.to_csv("")
        else:
            pass