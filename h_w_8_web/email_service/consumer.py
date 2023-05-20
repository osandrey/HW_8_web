import pika

import time
import json
from models import Contact




def send_email(message):
    print(f' [*] Email {message["payload"]} was successfully sent!')


def set_delivered(user_id):
    user = Contact.objects(id=user_id).first()
    user.is_delivered = True
    # print(user.name, user.is_delivered)
    user.save()



def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}")
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




