from datetime import datetime

now_str = "19931218"
now = datetime.strptime(now_str, "%Y%m%d")
now = now.strftime("%Y%m%d")
print(now)