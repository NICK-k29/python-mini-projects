# step-1 install required libraries
# pip install twilio
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step-2 twilio credentials
account_sid = 'ACb4416a30404ae27ee7a526304e30a89b'
auth_token = 'da6a7e30a5479ec950dc2339802d3cc5'

client = Client(account_sid, auth_token)

# step-3 send message
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Messgae SID {message.sid}')
    except Exception as e:
        print('An error occurred')

# step-4 user input
name = input('Enter the recipient name = ')
recipienr_number = input('Enter the recipient whatsapp number with country code = ')
message_body = input(f'enter the message {name}: ')

# step-5 parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24hour formate): ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%d-%m-%Y %H:%M')
current_datetime = datetime.now()

# calculate delay
time_diff = schedule_datetime - current_datetime
delay_seconds = time_diff.total_seconds()

if delay_seconds <= 0:
    print('Invalid date/time')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    # step-6 wait for the delay
    time.sleep(delay_seconds)

    # step-7 send the message
    send_whatsapp_message(recipienr_number, message_body)