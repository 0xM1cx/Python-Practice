import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC2302c0e6c2fd2cbe540820f6b8c3e43f']
auth_token = os.environ['d246e23a09dba65461ec0c76e0b2c1fb']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+639619381867',
                              body='The Game Will Now Commence',
                              to='+639771062549'
                          )