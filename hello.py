import pandas as pd

from core.util.ai.pandasai_util import PandasaiUtil

sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Taiwan", "Japan", "China", "Korea"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

pandasai_util = PandasaiUtil()
content = pandasai_util.analyze_data_with_chatgpt(sales_by_country, "DataFrame 是國家銷售額的資料", "找出銷售最高的國家？")

print(content)