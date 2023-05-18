
import certifi as certifi

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://osandreyman:1111@firstcluster.g6svumr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

db = client.test_db
records = db.privat


if __name__=='__main__':

    print('Підключення відбулось вдало!')
    print(f'Всього документів в цій БД: {records.count_documents({})}')





