from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Tweet

from .utils import *


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    return HttpResponse('Sign form is not yet created')


def home(request):
    if not request.user.is_authenticated:
        return redirect('sign-up')
    username = request.user.username
    user = User.objects.get(username=username)
    tweets = Tweet.objects.filter(author=user)
    follow_tweets = get_tweets(user, sample=3)
    side_follows = get_users(user, sample=5)
    side_trending_tags = get_trending_tags(user, sample=5)
    print(side_trending_tags)
    context = {
        'side_search': True,
        'side_follows': side_follows,
        'side_trending_tags': side_trending_tags,
        'nbar': 'home',
        'follow_tweets': follow_tweets,
        'tweets': tweets,
    }
    return render(request, 'tweets/home.html', context=context)


def explore(request):
    user = request.user
    side_follows = get_users(user, sample=5)
    trending_tags = get_trending_tags(user, sample=5)
    news = get_news(sample=8)

    context = {
        'side_follows': side_follows,
        'nbar': 'explore',
        'news': news,
        'trending_tags': trending_tags,
    }
    return render(request, 'tweets/explore.html', context=context)
