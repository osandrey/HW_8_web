import argparse

import certifi
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://osandreyman:1111@firstcluster.g6svumr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

db = client.cats

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
age = my_arg.get('age')
_id = my_arg.get('id')
features = my_arg.get('features')


class ExceptValidation(Exception):
    pass


def find_cats():
    return db.cats.find()


def find_cat(_id):
    return db.cats.find_one({'_id': ObjectId(_id)})


def create_cat(name_: str, age_: str, features_: list):
    result = db.cats.insert_one({"name": name_, "age": int(age_), "features": features_})
    return find_cat(result.inserted_id)


def update_cat(_id, name_: str, age_: str, features_: list):
    result = db.cats.update_one({'_id': ObjectId(_id)},
                                {'$set': {
                                    "name": name_,
                                    "age": int(age_),
                                    "features": features_
                                    }})
    print(result)
    return find_cat(_id)


def remove_cat(_id):
    result = db.cats.delete_one({'_id': ObjectId(_id)})
    return result


def main():
    try:
        match action:
            case 'create':
                res = create_cat(name, age, features)
                print(res)
            case 'find':
                res = find_cats()
                [print(cat) for cat in res]
            case 'update':
                res = update_cat(_id, name, age, features)
                print(res)
            case 'remove':
                res = remove_cat(_id)
                print(res)
            case _:

                print(f'Unknown command:')
    except ExceptValidation as error:
        print(f'Error is: {error}')


if __name__ == '__main__':
    main()
