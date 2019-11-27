import json
import asyncio
from urllib.parse import quote

from autobahn.asyncio.wamp import ApplicationRunner, ApplicationSession


class Component(ApplicationSession):
    async def onJoin(self, details):
        print(details)
        await self.register(self.authorizer, 'com.weather.authorize')
        await self.register(self.login, 'com.weather.login')

    async def authorizer(self, session, uri, action, options):
        if action != 'subscribe':
            return False

        cities = session.get('authextra', {}).get('cities', [])
        cities = [f'com.weather.city-{c}' for c in cities]

        return uri in cities

    async def login(self, realm, authid, details):
        print('------- login ---------', realm, authid)
        from pprint import pprint
        pprint(details['authextra'])

        print('-------------')
        # loop = asyncio.get_event_loop()
        session_id = details["authextra"]["token"]
        data2 = await self.call("com.myapp.get_cities",
                                method='GET',
                                url=f'{quote(session_id)}/')
        print('d2', data2)
        cities = await asyncio.get_event_loop().run_in_executor(
            None,
            json.loads,
            data2['content']
        )
        cities = cities['cities']
        return {
            'role': 'frontend',
            'authid': details["authextra"]["token"].split(':')[0],
            'extra': {
                'cities': cities
            }
        }


if __name__ == '__main__':
    realm = 'realm1'
    url = 'rs://localhost:8081'
    runner = ApplicationRunner(url, realm)
    runner.run(Component)
