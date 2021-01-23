import os
import datetime
from twilio.rest import Client



# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

time_now = datetime.datetime.now().strftime('%Y%m%d%s')


def easy_sms(msg, phone_number='+13038154080'):
    if not isinstance(msg, str):
        msg = str(msg)
    if not isinstance(phone_number, str):
        phone_number = str(phone_number)
    message = client.messages.create(
                                  from_='+13134838972',
                                  body=msg,
                                  to=phone_number
                              )

    return message.sid

def main():
    print(easy_sms(f'this message sent from main {time_now}'))


if __name__ == '__main__':
    main()
