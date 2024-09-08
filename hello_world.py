# print("Hello World!")
import yfinance as yf
import pandas as pd
import datetime as dt

from core.util.draw.stock_price_trend_chart_util import StockPriceTrendChartUtil


stock_price_trend_chart_util = StockPriceTrendChartUtil()

start = dt.datetime(2024, 9, 1)
end = dt.datetime(2024, 12, 31)

df_2330 = yf.download("2330.TW", start=start, end=end)
df_2454 = yf.download("2454.TW", start=start, end=end)

print(df_2330)

stock_price_trend_chart_util.plot_stock_price_trend(df_2330.Close, "TSMC", "TSMC", "Date", "Price")

# stock_price_trend_chart_util.plot_two_stock_price_trend(df_2330.Close, "TSMC", df_2454.Close, "MediaTek", "TSMC vs MediaTek", "Date", "Price")