# python script for sending message update
 
import time
from time import sleep
from sinchsms import SinchSMS
 
# function for sending SMS
def sendSMS():
 
    # enter all the details
    # get app_key and app_secret by registering
    # a app on sinchSMS
    number=''
    app_key = 'db152a07-277b-4d7c-a43e-1434c7c9cc45'
    app_secret = 'uyP5jU2QuUOiiyy441pPaA=='
 
    # enter the message to be sent
    message = "WHat else can I do"
 
    client = SinchSMS(app_key, app_secret)
    print("Sending '%s' to %s" % (message, number))
 
    response = client.send_message(number, message)
    message_id = response['messageId']
    response = client.check_status(message_id)
 
    # keep trying unless the status retured is Successful
    while response['status'] != 'Successful':
        print(response['status'],flush=True)
        time.sleep(1)
        response = client.check_status(message_id)
 
    print(response['status'])
 
if __name__ == "__main__":
    sendSMS()