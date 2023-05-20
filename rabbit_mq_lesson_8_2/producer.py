import datetime
import json
from random import randint

import pika

"""Креденшели доступу до бд"""

creds = pika.PlainCredentials('guest', 'guest')

"""Connection creation"""
host = 'localhost'
port = 5671
conn_string = pika.ConnectionParameters(host='localhost', port=5672, credentials=creds)
connection = pika.BlockingConnection(conn_string)
chanel = connection.channel()

"""Створити таску з типом 'direct' яка повязана з queue='task_queue'"""
chanel.exchange_declare(exchange='task_exchange', exchange_type='direct')
chanel.queue_declare(queue='task_queue', durable=True)
chanel.queue_bind(exchange='task_exchange', queue='task_queue')
"""Замість chanel.basic_publish(exchange='', routing_key='test', body='Test Message'.encode())"""

count = 0

while True:
    count += 1
    if count > 10:
        break

    message = {
        'id':count,
        'payload': randint(1, 3000),
        'date': datetime.datetime.now().isoformat()
    }

    chanel.basic_publish(
        exchange='task_exchange',
        routing_key='task_queue',
        body=json.dumps(message).encode(),
        properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
    )

    print(" [x] Sent %r" % message)

connection.close()


# chanel = connection.channel()
# chanel.queue_declare(queue='test')
#
# while True:
#     body = input('Message: ')
#     if body == 'Exit':
#         connection.close()
#         break
#     else:
#         chanel.basic_publish(exchange='', routing_key='test', body=body.encode())
#     # sleep(60)
#
