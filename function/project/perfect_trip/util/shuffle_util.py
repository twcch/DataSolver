import random


class ShuffleUtil():
    @staticmethod
    def shuffle_array(arr: list) -> object:
        index = random.randint(1, len(arr) - 1)
        return arr[index]
