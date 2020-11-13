from django.urls import path
from . import views

urlpatterns = [
    # Creates a route, which is brought into the main urls.py
    path('', views.index, name='index'),
]
