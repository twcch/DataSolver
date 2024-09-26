from function.project.perfect_trip.post_request.user_data_request import UserDataRequest


user_data_request = UserDataRequest("http://127.0.0.1:8080/api/users/register")
user_data_request.insert_data_to_user_master(10000)