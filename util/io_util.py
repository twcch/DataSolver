class IoUtil():

    def __init__(self):
        pass

    def read_file_to_dict(self, file_path, separator):
        data_dict = {}
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if separator in line:
                    key, value = line.split(separator, 1)
                    data_dict[key.strip()] = value.strip()

        return data_dict
