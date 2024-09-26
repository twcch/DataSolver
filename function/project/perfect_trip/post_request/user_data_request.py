from function.project.perfect_trip.util.shuffle_util import ShuffleUtil as su
import requests
import random


class UserDataRequest():
    def __init__(self, url):
        self.url = url

    def insert_data_to_user_master(self, number: int) -> None:
        for i in range(number):
            email = "aa" + str(random.randint(1, 9999)) + "@outlook.com"
            password = "123456"
            first_name = su.shuffle_array(["李", "張", "陸", "陳", "林"])
            last_name = su.shuffle_array(["小明", "小華", "小張", "小林", "小君"])
            nickname = su.shuffle_array(["Jack", "William", "Joy", "Tina", "Tim"])
            tax_id = (su.shuffle_array(["A", "B", "C"])
                      + str(random.randint(1, 2))
                      + str(random.randint(0, 9))
                      + str(random.randint(0, 9))
                      + str(random.randint(0, 9))
                      + str(random.randint(0, 9))
                      + str(random.randint(0, 9))
                      + str(random.randint(0, 9))
                      + str(random.randint(0, 9))
                      + str(random.randint(0, 9)))

            gender = su.shuffle_array(["MALE", "FEMALE"])
            phone_number = (str(0)
                            + str(random.randint(1, 2))
                            + str(random.randint(0, 9))
                            + str(random.randint(0, 9))
                            + str(random.randint(0, 9))
                            + str(random.randint(0, 9))
                            + str(random.randint(0, 9))
                            + str(random.randint(0, 9))
                            + str(random.randint(0, 9))
                            + str(random.randint(0, 9)))
            country = "TAIWAN"
            avatar = "image/100086623626067978"
            address = su.shuffle_array(["台北市", "新北市", "台中市"])

            data = {
                "username": email,
                "password": password,
                "firstName": first_name,
                "lastName": last_name,
                "nickname": nickname,
                "taxId": tax_id,
                "gender": gender,
                "phoneNumber": phone_number,
                "address": address
            }

            response = requests.post(self.url, json=data)
            print(response.status_code)
            print(response.text)
