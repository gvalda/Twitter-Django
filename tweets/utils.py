from django.contrib.auth.models import User
from .models import TweetTag, BigTweet


def get_users(user, sample=0):
    if user.is_authenticated:
        users = User.objects.exclude(username=user.username)
    else:
        users = User.objects.all()
    return users[:sample]


def get_tweets(user, sample=0):
    users = get_users(user=user, sample=sample)

    posts = []

    for user in users:
        user_posts = user.tweet_set.all()
        if user_posts:
            posts.append(user_posts[0])

        if len(posts) == sample:
            break

    return posts


def get_user_country(user):
    if user.is_authenticated:
        user_city = user.profile.current_city
        if user_city:
            return user_city.country
    return None


def get_trending_tags(user, sample=0):
    user_country = get_user_country(user)
    if user_country:
        tags = TweetTag.objects.filter(trending_countries=user_country)
    else:
        user_country = 'World'
        tags = TweetTag.objects.all()
    tags = sorted(tags, key=lambda x: x.tweet_set.count())
    tags = tags[:sample]
    local_trends = list(map(lambda x: (user_country, x), tags))
    return local_trends


def get_news(sample=0):
    big_tweets = BigTweet.objects.all()
    return big_tweets[:sample]
