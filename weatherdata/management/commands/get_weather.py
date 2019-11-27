import random
from urllib.request import urlopen, Request, URLError
import json

from django.core.management import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from ...models import WeatherData


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        layer = get_channel_layer()
        group_send = async_to_sync(layer.group_send)
        for data in WeatherData.objects.all():
            data.temperature = random.randint(-30, 50)
            group_send(
                f'weather-{data.pk}',
                {
                    "type": 'weather.update',
                    "city": data.pk,
                    "temperature": data.temperature,
                }
            )
            data.save()

            req = Request(
                url="http://localhost:8080/publish",
                headers={'Content-Type': 'application/json'},
                data=json.dumps({
                    'topic': f'com.weather.city-{data.pk}',
                    'kwargs': {
                        "type": 'weather.update',
                        "city": data.pk,
                        "temperature": data.temperature,
                        }}).encode(),
                method='POST')
            try:
                urlopen(req)
            except URLError:
                pass
