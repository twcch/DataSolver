import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import yfinance as yf


class StockPriceChartUtil():

    def __init__(self, ticker):
        self.__ticker = ticker
        self.__start_date = datetime.now() - relativedelta(years=1)
        self.__end_date = datetime.now()
        self.__data = yf.download(self.__ticker, start=self.__start_date, end=self.__end_date)

    def plot_stock_close_price_trend_chart(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.__data.Close, label=self.__ticker)
        plt.title(self.__ticker, loc="center")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True, axis="y")
        plt.legend()
        plt.show()

    def get_ticker(self) -> str:
        return self.__ticker

    def set_ticker(self, ticker: str) -> None:
        self.__ticker = ticker

    def get_start_date(self) -> datetime:
        return self.__start_date

    def set_start_date(self, start_date: datetime) -> None:
        self.__start_date = start_date

    def get_end_date(self) -> datetime:
        return self.__end_date

    def set_end_date(self, end_date: datetime) -> None:
        self.__end_date = end_date

    def get_data(self) -> pd.DataFrame:
        return self.__data

    def set_data(self, data: pd.DataFrame) -> None:
        self.__data = data
