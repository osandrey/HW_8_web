import certifi

from mongo_engine import Author, Quote

from mongoengine import connect

# Встановлення з'єднання з хмарною базою даних MongoDB
uri = "mongodb+srv://osandreyman:1111@firstcluster.g6svumr.mongodb.net/hw_8_web?retryWrites=true&w=majority"
connection = connect(host=uri,  tlsCAFile=certifi.where(), ssl=True)


def get_all_authors():
    authors = Author.objects()
    for author in authors:
        print(author.to_mongo().to_dict())


def get_all_quotes():
    quotes = Quote.objects()
    for quote in quotes:
        print(quote.to_mongo().to_dict())


# Функція для пошуку цитат за тегом
def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    print("Цитати за тегом '{}':".format(tag))
    for quote in quotes:
        print("- {}".format(quote.quote))
    print()


# Функція для пошуку цитат за ім'ям автора
def search_by_author(author_fullname):
    auth = Author.objects(fullname=author_fullname).first()
    if author:
        quotes = Quote.objects(author=auth)
        print("Цитати автора '{}':".format(author_fullname))
        for quote in quotes:
            print("- {}".format(quote.quote))
    else:
        print("Автор '{}' не знайдений.".format(author_fullname))
    print()


# Функція для пошуку цитат за набором тегів
def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    print("Цитати з тегами '{}':".format(tags))
    for quote in quotes:
        print("- {}".format(quote.quote))
    print()


# Основний цикл виконання скрипту
if __name__ == '__main__':
    while True:
        command = input("Введіть команду (name:<author>, tag:<tag>, tags:<tag1,tag2>, або exit): ")
        parts = command.split(':')

        if parts[0] == 'name':
            author = parts[1].strip()
            search_by_author(author)
        elif parts[0] == 'tag':
            tag = parts[1].strip()
            search_by_tag(tag)
        elif parts[0] == 'tags':
            tags = parts[1].strip()
            search_by_tags(tags)
        elif parts[0] == 'exit':
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")







