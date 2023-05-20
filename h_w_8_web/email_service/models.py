import certifi
from mongoengine import *


uri = "mongodb+srv://osandreyman:1111@firstcluster.g6svumr.mongodb.net/hw_8_web?retryWrites=true&w=majority"
connection = connect(host=uri,  tlsCAFile=certifi.where(), ssl=True)


class Contact(Document):
    """ім'я, email та логічне поле"""

    name = StringField(max_length=100, min_length=4)
    email = StringField(max_length=40, min_length=4)
    is_delivered = BooleanField(default=False)


"""Під час запуску скрипта producer.py він генерує певну кількість фейкових
контактів та записує їх у базу даних. Потім поміщає у чергу RabbitMQ повідомлення,
яке містить ObjectID створеного контакту, і так для всіх згенерованих контактів."""

