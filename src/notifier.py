import os
import datetime
from twilio.rest import Client



# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

time_now = datetime.datetime.now().strftime('%Y%m%d%s')


def easy_sms(msg, phone_numbers=['+13038154080', '+18018147058']):
    if not isinstance(msg, list):
        msg = str(msg)
    if not isinstance(phone_numbers, list):
        phone_numbers = [phone_numbers]
    out = []
    for phone_number in phone_numbers:
        out.append(client.messages.create(
                                      from_='+13134838972',
                                      body=msg,
                                      to=phone_number
                                  )
                    )

    return out

def main():
    print(easy_sms(f'this message sent from main {time_now}'))


if __name__ == '__main__':
    main()
