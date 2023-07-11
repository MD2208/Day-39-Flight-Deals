#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from data_manager import UserManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data = DataManager()
sheet_data= data.sheet_data

## Adding users to do data
first_name = str(input("Welcome to Melih's Flight Club.\nWhat is your first name? "))
last_name = str(input("What is your last name? "))
email= str(input("What is your email address? "))
repeat_email = str(input("Please repeat your email: "))
if (email == repeat_email):
    user = UserManager()
    user.set_user(first_name,last_name,email)
else:
    print('Validation Error!')

## Getting user from data
users = UserManager()
user_mails = users.get_users()

### Flight Deals and notifications
for row in sheet_data:
    flight_search = FlightSearch(row['city'])
    if row['iataCode']=='':
        data.put_IATA_kod(row['id'],flight_search.IATA_kod)
    else:
        flight_data = flight_search.check_flights('KRK',flight_search.IATA_kod)
        if(flight_data != None and flight_data.price <= row['lowestPrice']):
            notify = NotificationManager(flight_data.price,flight_data.origin_city,
                                flight_data.origin_airport,flight_data.destination_city,
                                flight_data.destination_airport,flight_data.out_date,
                                flight_data.return_date)
            message=f"Low price alert! Only {flight_data.price}euro to fly\nfrom {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}\nfrom {flight_data.out_date} to {flight_data.return_date}."
            notify.send_emails(user_mails,message)
            pass
