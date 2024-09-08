class KeyUtil():

    def __init__(self):
        self.__key_folder = "/Users/twcch/Documents/Code/_keys"

    def get_chatgpt_api_key(self):
        file = open(self.__key_folder + "/openai_key.txt", "r")
        api_key = file.read()

        return api_key