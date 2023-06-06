import pika
import smtplib
import ssl
import time
import json
from models import Contact
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(message):
    # print(f' [*] Email {message["payload"]} was successfully sent!')
    user_name = message.get('payload')[0]
    print(user_name)
    Host = 'smtp.gmail.com'
    Port = 587
    Sender = 'osandreyman@gmail.com'
    Sender_password = ********

    # Enter your address
    target_email = message.get("payload")[1]
    receiver_email = target_email  # Enter receiver address
    # password = input("Type your password and press enter: ")
    # email_message = f"Subject: Hi {message.get('payload')[0]}\n {message.get('text')}"
    context = ssl.create_default_context()
    with smtplib.SMTP(Host, Port) as server:
        try:
            context.check_hostname = False
            server.starttls(context=context)
            server.login(Sender, Sender_password)

            message = MIMEMultipart()
            message['From'] = Sender
            message['To'] = receiver_email
            message['Subject'] = f"Subject: Hi {user_name}"
            message.attach(MIMEText(message.get('text'), 'plain', 'utf-8'))
        except Exception as err:
            print(f'MY ERROR IS: {err}')

def set_delivered(user_id):
    user = Contact.objects(id=user_id).first()
    if user:

        user.is_delivered = True
    # print(user.name, user.is_delivered)
        user.save()
    else:
        print('User was not found!')



def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}, {type(message)}")
    send_email(message)
    set_delivered(message["id"])
    time.sleep(1)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)



def consumer_service():

    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    '''Підключення до queue та callback'''
    channel.basic_consume(queue='email_queue', on_message_callback=callback)

    channel.start_consuming()




if __name__ == '__main__':

    while True:
        consumer_service()




