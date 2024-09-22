import os


class PathUtil():

    user_folder = os.path.expanduser("~")
    desktop = os.path.join(user_folder, "Desktop")
    downloads = os.path.join(user_folder, "Downloads")
    documents = os.path.join(user_folder, "Documents")
    drive = os.path.join(documents, "Drive")
    data = os.path.join(drive, "Data")

    code_folder = os.path.join(documents, "Code")
    datascience_folder = os.path.join(code_folder , "DataScience")
    keys_folder = os.path.join(code_folder, "_keys")

    temp_data_folder = "./temp/data"
