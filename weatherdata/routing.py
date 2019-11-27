from django.urls import path

from .consumers import WeatherUpdateConsumer


websocket_urlpatterns = [
    path('ws/update/', WeatherUpdateConsumer)
]
