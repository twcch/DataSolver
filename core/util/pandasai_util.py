import os
import pandas as pd
from pandasai import Agent
from pandasai.llm import OpenAI


class PandasAIUtil():
    os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

    def __init__(self):
        self.__llm = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def analyze_data_with_chatgpt(self, data: pd.DataFrame, data_description: str, query_message: str) -> pd.DataFrame:
        agent = Agent(data, description=data_description, config={"llm": self.__llm})

        response = agent.chat(query_message)

        return response
