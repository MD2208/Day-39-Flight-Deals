import requests
import datetime as dt
from flight_data import FlightData
FLIGHT_SEARCH_API_KEY = "your-tequila-api-key"
locations_search_end_point = 'https://api.tequila.kiwi.com/locations/query'
headers = {
    'apikey':FLIGHT_SEARCH_API_KEY
}
search_end_point = "https://api.tequila.kiwi.com/v2/search"
### Time Calc #### 
now = dt.datetime.now()
tomorrow= now + dt.timedelta(1)
tomorrow = tomorrow.strftime("%d/%m/%Y")
in_2_months = now + dt.timedelta(60)
in_2_months = in_2_months.strftime("%d/%m/%Y")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,city_name):
        self.city=city_name
        self.get_IATA_kod()
    
    def get_IATA_kod(self):
        params = {
            "term":self.city,
            "location_types": "city"
        }
        get_req = requests.get(url=locations_search_end_point, params=params, headers=headers)
        self.IATA_kod=get_req.json()['locations'][0]['code']
    
    def check_flights(self, origin_city_code, destination_city_code):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": tomorrow,
            "date_to": in_2_months,
            "nights_in_dst_from": 4,
            "nights_in_dst_to": 9,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        find_flight_req = requests.get(
            url=f"{search_end_point}",
            headers=headers,
            params=query,
        )
        
        try:
            data = find_flight_req.json()["data"][0]
        except IndexError:
            query['max_stopovers']=1
            response = requests.get(
                url=f"{search_end_point}",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
            except IndexError:
                print('There is no flight')
                return None
            else:
                flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city= data["route"][0]["cityTo"]
            )
                return flight_data
        else: 
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data