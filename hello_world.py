import pandas as pd

data = {
    "給付項目": "A101",
    "年度起": 0,
    "年度末": 4,
    "金額": 1000
}

print(f"被保險人於保單年度 {data.get('年度起')} "
      f"至 {data.get('年度末')} 身故，給付理賠金額 {data.get('金額')}"
      )
