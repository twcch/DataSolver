import os
import pandas as pd
from pandasai import Agent
from pandasai.llm import OpenAI

from backup.core.util.key_util import KeyUtil


class PandasaiUtil():

    def __init__(self):
        self.__key_util = KeyUtil()
        self.__api_key = self.__key_util.get_chatgpt_api_key()
        os.environ["OPENAI_API_KEY"] = self.__api_key
        self.__llm = OpenAI(api_token=os.environ["OPENAI_API_KEY"])

    def analyze_data_with_chatgpt(self, data: pd.DataFrame, data_description: str, query_message: str) -> pd.DataFrame:
        agent = Agent(data, description=data_description, config={"llm": self.__llm})

        response = agent.chat(query_message)

        return response