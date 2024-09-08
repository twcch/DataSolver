import pandas as pd
import matplotlib.pyplot as plt


class StockPriceTrendChartUtil():

    def __init__(self):
        pass

    def plot_stock_close_price_trend(self,
                               data: pd.DataFrame,
                               label: str,
                               title: str,
                               xlabel: str,
                               ylabel: str):
        plt.figure(figsize=(10, 6))
        plt.plot(data, label=label)
        plt.title(title, loc="center")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, axis="y")
        plt.legend()
        plt.show()

    # def plot_two_stock_price_trend(self,
    #                                data_1: pd.DataFrame,
    #                                data_1_label: str,
    #                                data_2: pd.DataFrame,
    #                                data_2_label: str,
    #                                title: str,
    #                                xlabel: str,
    #                                ylabel: str):
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(data_1, label=data_1_label)
    #     plt.plot(data_2, label=data_2_label)
    #     plt.title(title, loc="center")
    #     plt.xlabel(xlabel)
    #     plt.ylabel(ylabel)
    #     plt.grid(True, axis="y")
    #     plt.legend()
    #     plt.show()