import pandas as pd

from core.util.file_util import FileUtil


file_util = FileUtil()

data = pd.DataFrame({"A": [1, 2, 3],
                     "B": [4, 5, 6]})

print(file_util.generate_temp_file(data))