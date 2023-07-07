#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data = DataManager()
sheet_data= data.sheet_data

for row in sheet_data:
    flight_search = FlightSearch(row['city'])
    if row['iataCode']=='':
        data.put_IATA_kod(row['id'],flight_search.IATA_kod)
    else:
        flight_data = flight_search.check_flights('KRK',flight_search.IATA_kod)
        if(flight_data != None and flight_data.price <= row['lowestPrice']):
            NotificationManager(flight_data.price,flight_data.origin_city,flight_data.origin_airport,flight_data.destination_city,flight_data.destination_airport,flight_data.out_date,flight_data.return_date)

