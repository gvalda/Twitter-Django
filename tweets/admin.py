from django.contrib import admin
from .models import *


class TweetImageInline(admin.TabularInline):
    model = TweetImage


class TweetAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

    inlines = [
        TweetImageInline,
    ]


class TweetTagAdmin(admin.ModelAdmin):
    filter_horizontal = ('trending_countries', 'categories')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(BigTweet)
admin.site.register(TweetImage)
admin.site.register(TweetTag, TweetTagAdmin)
