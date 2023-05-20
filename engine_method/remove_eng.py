from mongo_engine import Post, User


if __name__ == '__main__':

    post = Post.objects(id='646600e7dbaa5433f897d5ff')
    print(post)
    for p in post:
        print(p.to_mongo().to_dict())
    result = post.delete()

    post = Post.objects(id='646600e7dbaa5433f897d600')
    print(post)
    for p in post:
        print(p.to_mongo().to_dict())
    result = post.delete()

    user = User.objects(id='646600e7dbaa5433f897d5fd')
    user.delete()

    user = User.objects(id='646600e7dbaa5433f897d5fe')
    user.delete()