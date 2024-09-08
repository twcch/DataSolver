class KeyUtil():

    def __init__(self):
        self.__key_folder = "/Users/twcch/Documents/DataScience/_keys"

    def get_chatgpt_api_key(self):
        file = open(self.__key_folder + "/chatgpt_api_key.txt", "r")
        api_key = file.read()

        return api_key
