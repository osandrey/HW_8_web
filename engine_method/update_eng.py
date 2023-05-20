from mongo_engine import Post, User


if __name__ == '__main__':

    post = Post.objects(id='646605c608eddde0059b86b3')
    print(post)
    for p in post:
        print(p.to_mongo().to_dict())
        print(p.link_url)
    result = post.update(link_url='https://docs.mongoengine.org/tutorial.html')
    print(post[0].to_mongo().to_dict())