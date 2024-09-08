from openai import OpenAI
from util.path_util import PathUtil


class ChatgptUtil():

    def __init__(self, model="gpt-3.5-turbo"):
        self.__path_util = PathUtil()
        self.__api_key = self.__get_openai_key()
        self.__model = model
        self.__client = OpenAI(api_key=self.__api_key)
        self.__chatgpt_role = "你是我的助手，根據問題使用繁體中文回覆"

    def chat_with_chatgpt(self, message):
        chatgpt_role = self.__chatgpt_role

        response = self.__client.chat.completions.create(
            model=self.__model,
            messages=[
                {"role": "assistant", "content": chatgpt_role},
                {"role": "user", "content": message}
            ]
        )

        content = response.choices[0].message.content

        return content

    def set_model(self, model):
        self.__model = model

    def set_chatgpt_role(self, chatgpt_role):
        self.__chatgpt_role = chatgpt_role

    def __get_openai_key(self):
        with open(self.__path_util.get_keys_folder() + "/openai_key.txt", "r") as file:
            api_key = file.read()

        return api_key
