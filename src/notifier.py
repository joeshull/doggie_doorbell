import os
import datetime
from twilio.rest import Client



# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_FROM_NUMBER']

client = Client(account_sid, auth_token)

def easy_sms(msg, phone_number):
    if not isinstance(msg, list):
        msg = str(msg)
    if not isinstance(phone_number, str):
        phone_number = str(phone_number)
    msg = client.messages.create(from_=twilio_number,
                                 body=msg,
                                 to=phone_number
                                 )
    return msg

def sms_multiple_numbers(msg, phone_numbers):
    if not isinstance(phone_numbers, list):
        phone_numbers = [phone_numbers]
    out = []
    for num in phone_numbers:
        out.append(easy_sms(msg, num))
    return out


def main():
    time_now = datetime.datetime.now().strftime('%Y%m%d%s')
    print(easy_sms(f'this message sent from main {time_now}'))


if __name__ == '__main__':
    main()
