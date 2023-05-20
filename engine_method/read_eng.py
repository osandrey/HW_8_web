from mongo_engine import Post, User

"""(p.to_mongo().to_dict())/p.to_json()"""
if __name__ == '__main__':

    post = Post.objects()
    for p in post:
        print(p.to_mongo().to_dict())

    users = User.objects()
    for user in users:
        print(user.to_mongo().to_dict())


    # for post in Post.objects:
    #     print(post.title)
    #     print('=' * len(post.title))
    #
    #     if isinstance(post, TextPost):
    #         print(post.content)
    #
    #     if isinstance(post, LinkPost):
    #         print('Link: {}'.format(post.link_url))