import random

class RandomUtil():

    @staticmethod
    def random_int(min, max) -> int:
        return random.randint(min, max)

    @staticmethod
    def random_float(min, max) -> float:
        return random.uniform(min, max)

    @staticmethod
    def random_bool() -> bool:
        return random.choice([True, False])

    @staticmethod
    def random_elementor_from_list(l) -> list:
        return random.choice(l)