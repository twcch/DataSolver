from openai import OpenAI
from util.path_util import PathUtil


class ChatgptUtil():

    def __init__(self):
        self.__path_util = PathUtil()
        self.__api_key = self.__get_openai_key()
        self.__model = None
        self.__client = OpenAI(api_key=self.__api_key)
        self.__chatgpt_role = "你是我的助手，根據問題使用繁體中文回覆"

    # 使用 chatgpt 3.5 model
    def chat_with_chatgpt3(self, message):
        content = self.__chat_with_chatgpt("gpt-3.5-turbo", message)

        return content

    # 使用 chatgpt 4 model
    def chat_with_chatgpt4(self, message):
        content = self.__chat_with_chatgpt("gpt-4-turbo", message)

        return content

    # 使用自定義模型
    def chat_with_chatgpt(self, message):
        if self.__model == None:
            raise ValueError("Null exception: 請設定 ai model")

        content = self.__chat_with_chatgpt(self.__model, message)

        return content

    def set_model(self, model):
        self.__model = model

    def set_chatgpt_role(self, chatgpt_role):
        self.__chatgpt_role = chatgpt_role

    def __chat_with_chatgpt(self, model, message):
        chatgpt_role = self.__chatgpt_role

        response = self.__client.chat.completions.create(
            model=model,
            messages=[
                {"role": "assistant", "content": chatgpt_role},
                {"role": "user", "content": message}
            ]
        )

        content = response.choices[0].message.content

        return content

    def __get_openai_key(self):
        with open(self.__path_util.get_keys_folder() + "/openai_key.txt", "r") as file:
            api_key = file.read()

        return api_key
