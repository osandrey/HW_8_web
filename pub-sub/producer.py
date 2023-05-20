import pika

"""Підписатися до брокера"""
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

"""Генерація події"""
"""Декларуємо біржу"""

channel.exchange_declare(exchange='logs', exchange_type='fanout')

if __name__ == '__main__':
    channel.basic_publish(exchange='logs', routing_key='', body='Hello Andrii'.encode())
    connection.close()