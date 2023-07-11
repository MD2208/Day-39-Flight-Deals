import requests
SHEETY_API_KEY = 'your-sheety-api-key'
flights_url= f"https://api.sheety.co/{SHEETY_API_KEY}/flightDeals/"
prices_end_point = f"{flights_url}prices"
users_end_point = f"{flights_url}users"

class DataManager:
    def __init__(self):
        self.get_flights_data()

    def get_flights_data(self):
        get_req = requests.get(url=prices_end_point)
        self.sheet_data = get_req.json()['prices']
    
    def put_IATA_kod(self,row_id,kod):
        body= {
            'price':{
            'iataCode':kod
            }
        }
        put_req = requests.put(f"{prices_end_point}/{row_id}",json=body)
        # print(put_req.text)

class UserManager:
    def __init__(self):
        self.note = 'This is for user data'

    def set_user(self,first_name,last_name,email):
        body={
            'user':{
                'firstName':first_name,
                'lastName':last_name,
                'email':email
            }
        }
        post_req = requests.post(users_end_point, json=body)
        print(post_req.text)
    def get_users(self):
        get_req = requests.get(users_end_point)
        user_mails =[user['email'] for user in get_req.json()['users']]
        return user_mails
        