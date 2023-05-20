import json
import time

import pika
from time import sleep

"""Креденшели доступу до бд"""

creds = pika.PlainCredentials('guest', 'guest')

"""Connection creation"""
host = 'localhost'
port = 5671
conn_string = pika.ConnectionParameters(host='localhost', port=5672, credentials=creds)
connection = pika.BlockingConnection(conn_string)
chanel = connection.channel()

"""Слухати все з queue='task_queue'"""
chanel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for message. To exit press CTRL+C')


def callback(ch, method, properties, body):
    """Шось робить, коли отримаєтся мєседж. Обовязково має 4 параметру"""
    '''Коли подія станется всі арги заповнятся автоматом'''
    message = json.loads(body)
    print(' [*] Received %r' % message)

    time.sleep(1)
    print(' [*] Done!')
    ch.basic_ack(delivery_tag=method.delivery_tag)


"""Вивожити по одному запису"""
chanel.basic_qos(prefetch_count=1)
"""Відправити команду брокеру та пов'язує"""
chanel.basic_consume(queue='task_queue', on_message_callback=callback)

# chanel.basic_consume(queue='test', on_message_callback=callback)
chanel.start_consuming()
# # chanel.stop_consuming()
