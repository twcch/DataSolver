import random

class RandomUtil():

    @staticmethod
    def random_int(min, max):
        return random.randint(min, max)

    @staticmethod
    def random_float(min, max):
        return random.uniform(min, max)

    @staticmethod
    def random_bool():
        return random.choice([True, False])

    @staticmethod
    def random_elementor_from_list(l):
        return random.choice(l)