from django.db import models
from django.conf import settings


# Create your models here.
class WeatherData(models.Model):
    CLOUDS_CLEAR = 1
    CLOUDS_PARTLY = 2
    CLOUDS_CLOUDY = 3
    CLOUDS = (
        (CLOUDS_CLEAR, 'clear'),
        (CLOUDS_PARTLY, 'partly cloudy'),
        (CLOUDS_CLOUDY, 'cloudy')
    )

    city = models.CharField(max_length=250)
    city_api_id = models.BigIntegerField(db_index=True, null=True, unique=True)

    temperature = models.SmallIntegerField(default=0)
    clouds = models.SmallIntegerField(choices=CLOUDS, default=1)

    subscribed_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.city
