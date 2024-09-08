import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
from dateutil.relativedelta import relativedelta


class PandasDataReaderUtil():

    def __init__(self,
                 start_date=datetime.now() - relativedelta(years=1),
                 end_date=datetime.now()):
        self.start_date = start_date
        self.end_date = end_date

    def get_stock_data(self, ticker: str) -> pd.DataFrame:
        data = web.get_data_yahoo("GOOG", start=self.start_date, end=self.end_date)

        return data

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date