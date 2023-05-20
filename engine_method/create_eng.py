from mongo_engine import Post, LinkPost, ImagePost, TextPost, User



if __name__=='__main__':
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
    andy = User(email='andy@google.com', first_name='Andy', last_name='Osyp').save()

    post1 = TextPost(title='Fun with MongoEngine', author=andy)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']

    post1.save()

    post2 = ImagePost(title='Steve Photo', author=ross)
    post2.image_path = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/lQKdHMxfYcCBOvwRKBAxPZVNtkg.jpg'
    post2.tags = ['actor']
    post2.save()

    post2 = LinkPost(title='MongoEngine Documentation', author=ross)
    post2.link_url = 'http://docs.mongoengine.com/'
    post2.tags = ['mongoengine']
    post2.save()