from datetime import datetime
import pandas as pd

import tejapi
from core.util.key_util import KeyUtil
from core.constant.data_table import DataTable


class TejDataUtil():
    tejapi.ApiConfig.api_key = KeyUtil().get_tej_api_key()

    def __init__(self):
        self.__now_str = datetime.now().strftime("%Y%m%d")

    def download_all_data(self, desc: str, tables=None) -> None:
        if tables is None:
            table_dict = DataTable.tej_test_table_dict
            for table in table_dict.keys():
                values = table_dict[table]
                data = pd.DataFrame(tejapi.get(values))
                data.to_csv(desc + "/" + table + "_v" + self.__now_str + ".csv", index=False)
        elif tables is not None:
            for table in tables:
                data = pd.DataFrame(tejapi.get(table))
                data.to_csv(desc + "/" + table + "_v" + self.__now_str + ".csv", index=False)