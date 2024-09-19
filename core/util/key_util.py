class KeyUtil():

    def __init__(self):
        self.__key_folder = "/Users/twcch/Documents/Code/_keys"

    def get_chatgpt_api_key(self) -> str:
        file = open(self.__key_folder + "/openai_key.txt", "r")
        api_key = file.read()

        return api_key

    def get_tej_api_key(self) -> str:
        file = open(self.__key_folder + "/tej_key.txt", "r")
        api_key = file.read()

        return api_key