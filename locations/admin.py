from django.contrib import admin
from .models import *


class CityInline(admin.TabularInline):
    model = City


class CountryAdmin(admin.ModelAdmin):
    inlines = [
        CityInline,
    ]


class CountryInline(admin.TabularInline):
    model = Country


class ContinentAdmin(admin.ModelAdmin):
    inlines = [
        CountryInline
    ]


admin.site.register(City)
admin.site.register(Country, CountryAdmin)
admin.site.register(Continent, ContinentAdmin)
