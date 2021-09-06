from django.db import models

import uuid


class Category(models.Model):
    category = models.CharField(max_length=25, unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category
