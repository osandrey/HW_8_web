import time
import pika
from datetime import datetime
import json
import faker
from models import Contact

CONTACTS_NUMBER = 50
fake_data = faker.Faker('uk_UA')

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='email_service', exchange_type='direct')
channel.queue_declare(queue='email_queue', durable=True)
channel.queue_bind(exchange='email_service', queue='email_queue')


def generate_fake_data(contact_number) -> tuple():
    # тут зберігатимемо співробітників

    for _ in range(contact_number):
        contact = Contact(name=fake_data.name(), email=fake_data.email())
        contact.save()

    # Згенеруємо тепер number_employees кількість співробітників'''


def main():

    contacts = Contact.objects()
    for contact in contacts:

        message = {
            "id": str(contact.id),
            "payload": [contact.name, contact.email],
            "date": datetime.now().isoformat(),
            "text": 'Try my  first Telegram Bot: https://t.me/ChefHelperBot'
            }

        channel.basic_publish(
            exchange='email_service',
            routing_key='email_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)
        time.sleep(1)
    connection.close()


if __name__ == '__main__':
    main()
    """For generate fake contacts and add them to DB"""
    # generate_fake_data(CONTACTS_NUMBER)
