from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('', views.sign_up, name='sign-up'),
]
