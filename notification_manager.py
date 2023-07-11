import smtplib
from twilio.rest import Client
from flight_data import FlightData

account_sid = "your-sid"
auth_token = "your-token"
MY_EMAIL =  'your-mail'
MY_PASSWORD = 'your-app-pass'

class NotificationManager(FlightData):
    def __init__(self,price,origin_city,origin_airport,destination_city,destination_airport,out_date,return_date):
            super().__init__(price,origin_city,origin_airport,destination_city,destination_airport,out_date,return_date)
            self.send_notifications()
    def send_notifications(self):
    
        client = Client(account_sid, auth_token)
        client.messages.create(
                            body=f"Low price alert! Only €{self.price} to fly\n"
                            f"from {self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport}\n"
                            f"from {self.out_date} to {self.return_date}.",
                            from_='your-twilio-numb',
                            to='reciever'
                        )
    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )