import tejapi
import pandas as pd

tejapi.ApiConfig.api_key = "rcL33ZVZvsWv8zABbNOm3pBI3DxRKc"
data = pd.DataFrame(tejapi.get('TRAIL/TAOFCAN'))

data.to_csv("/Users/twcch/Documents/Drive/Data/TEJ/test_database/TRAIL_TAOFCAN_v20240920.csv")