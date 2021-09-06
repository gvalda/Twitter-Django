from django.db import models

from django.contrib.auth.models import User
from locations.models import *

import os


def get_upload_path(instance, filename):
    return os.path.join(instance.user.username, f'profile-picture.{os.path.splitext(filename)[-1]}')


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to=get_upload_path, default='images/default.jpg')
    current_city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def get_image(self):
        try:
            url = self.profile_image.url
        except:
            self.profile_image = 'images/default.jpg'
            self.save()
            url = self.profile_image.url
        return url
