import requests
SHEETY_API_KEY = 'your-sheety-api'
flights_doc_end_point= f"https://api.sheety.co/{SHEETY_API_KEY}/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.get_flights_data()

    def get_flights_data(self):
        get_req = requests.get(url=flights_doc_end_point)
        self.sheet_data = get_req.json()['prices']
    
    def put_IATA_kod(self,row_id,kod):
        body= {
            'price':{
            'iataCode':kod
            }
        }
        put_req = requests.put(f"{flights_doc_end_point}/{row_id}",json=body)
        # print(put_req.text)