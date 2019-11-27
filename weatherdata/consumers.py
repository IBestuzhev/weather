from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async


class WeatherUpdateConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        assert self.channel_layer is not None
        if not self.scope['user'].is_authenticated:
            return await self.close()
        await self.accept()
        ids = await (database_sync_to_async(self.get_user_data)(self.scope['user']))
        for city_id in ids:
            group_name = f'weather-{city_id}'
            self.groups.append(group_name)
            await self.channel_layer.group_add(group_name, self.channel_name)

    def get_user_data(self, user):
        data = user.weatherdata_set.all()
        data = data.values_list('pk', flat=True)
        return list(data)

    async def weather_update(self, message):
        await self.send_json(message)
