from django.db import models

import uuid


class Continent(models.Model):
    continent = models.CharField(max_length=200, unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.continent


class Country(models.Model):
    country = models.CharField(max_length=200, unique=True)
    contient = models.ForeignKey(Continent, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city
