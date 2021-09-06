from django.db import models
from django.utils.timezone import utc

from django.contrib.auth.models import User
from locations.models import Country
from categories.models import Category

import uuid
import os
from datetime import datetime


def get_tweetimage_upload_path(instance, filename):
    return os.path.join(str(instance.tweet.author), 'tweets', str(instance.tweet.id), filename)


def get_bigtweet_upload_path(instance, filename):
    return os.path.join('big_tweets', str(instance.id), filename)


class TweetTag(models.Model):
    tag = models.CharField(max_length=25, unique=True)
    categories = models.ManyToManyField(Category)
    trending_countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return self.tag


class Tweet(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    parent_tweet = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(TweetTag, blank=True)
    comments = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    posted = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.description[:50]

    @property
    def get_posted(self):
        try:
            now = datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.posted
            total_seconds = timediff.total_seconds()
            hours_passed = int(total_seconds // 3600)
            return f'{hours_passed}h'
        except:
            return 'Error in date calculations'


class BigTweet(models.Model):

    featured_image = models.ImageField(
        upload_to=get_bigtweet_upload_path, default='images/default.jpg')
    header = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    @property
    def get_image(self):
        try:
            url = self.featured_image.url
        except:
            self.featured_image = 'images/default.jpg'
            self.save()
            url = self.featured_image.url
        return url

    @property
    def get_posted(self):
        try:
            now = datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.posted
            total_seconds = timediff.total_seconds()
            hours_passed = int(total_seconds // 3600)
            return f'{hours_passed}h'
        except:
            return 'Error in date calculations'

    def __str__(self):
        return self.header


class TweetImage(models.Model):

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=get_tweetimage_upload_path, default='images/default.jpg')
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.tweet.description[:50]

    @property
    def get_image(self):
        try:
            url = self.image.url
        except:
            self.image = 'images/default.jpg'
            self.save()
            url = self.image.url
        return url
