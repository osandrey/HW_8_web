# from pymongo import MongoClient
#
# client = MongoClient('mongodb+srv://username:password@localhost')
# # client = MongoClient('mongodb://admin:admin@localhost')
# db = client.users  """users назва БД"""
#
# db.users.insert_one({'name':'Andrii', 'age': 30})
# result = db.users.find({})
#
# for document in result:
#     print(document)


###ODM Mapper let us mapp Python objects to mongo objects
from mongoengine import connect, Document, EmbeddedDocument
from mongoengine.fields import StringField, IntField

connection = connect(host='mongodb+srv://username:password@localhost')

class Record(EmbeddedDocument):
    pass

class User(Document):
    name = StringField()
    age = IntField()
    record = Record()

#Щоб створити достатньо інстенсмювати.

user_1 = User(name='Jack')
connection
