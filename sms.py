# auth token 8907e99183066427cb12a4f564a4a1af
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "your acc"
auth_token = 'your auth token'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="content of your message",
  from_="your twilio number",
  to="reciever's number"
)

print(message.sid)