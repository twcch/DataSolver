from openai import OpenAI

from util.key_util import KeyUtil


class ChatgptUtil():

    def __init__(self):
        self.__key_util = KeyUtil()
        self.__api_key = self.__key_util.get_chatgpt_api_key()
        self.__model = None
        self.__client = OpenAI(api_key=self.__api_key)
        self.__chatgpt_role = "你是我的助手，根據問題使用繁體中文回覆"

    # 使用 chatgpt 3.5 model
    def chat_with_chatgpt3(self, message):
        response = self.__chat_with_chatgpt("gpt-3.5-turbo", message)

        return response

    # 使用 chatgpt 4 model
    def chat_with_chatgpt4(self, message):
        response = self.__chat_with_chatgpt("gpt-4-turbo", message)

        return response

    # 使用自定義模型
    def chat_with_chatgpt(self, message):
        if self.__model == None:
            raise ValueError("Null exception: 請設定 ai model")

        response = self.__chat_with_chatgpt(self.__model, message)

        return response

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
