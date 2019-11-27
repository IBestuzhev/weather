# Weather Data

Here you have quite a basic application.

So far it allows user to login/register and access dashboard.

User can subscribe to any city he wants.  
And on dashboard he can see list of cities he is subscribed to 
and current temperature.

There is no real API for now, data is completely random

## Your task

There are 2 primary tasks that you need to implement.

### Integrate the API

You have to upgrade the management command to use real API to download weather data. Also you can use any background tasks system.

It's up to you what weather provider to use. But please pick the free one.

#### Want to score more points? Consider the following:

* **Token security** (in case you use API that requires registration) - You will probably use the API provider that requires registration and obtaining API Token. Treat it seriously, even though this is free access. You should provide the instructions how to get the token, but don't store the token unencrypted in the repo
* **User Input Validation** - When user enters the city name - ensure it is available through API.
* **Rate Limit** - Imagine you have 100 cities, but your API allows only 60 requests per minute. The background task that you implement should be ready to handle it.
* **Test mode** - Perhaps you should keep random data generation for easier testing.

### Make it all real-time

As a user, I don't want to reload the page to see weather change.

Avoid AJAX-polling - you **can not** request new data every minute.  
The page should open the websocket connection and subscribe to changes.

It's up to you what websocket server to use.

Some examples:

* Use separate async server like [aiohttp](https://aiohttp.readthedocs.io/en/stable/) or [Tornado](https://www.tornadoweb.org/en/stable/)
* Keep it all in Django with [Django Channels](https://channels.readthedocs.io/en/latest/)
* Use higher level server, like [Crossbar](https://crossbar.io/), that implements publish-subscribe

#### Please keep in mind:

It's optional, but it would be nice to implement

1. **Traffic** - Don't spam user, do not send an update about cities user is not subscribed to.
1. **Security** - It should be impossible to listen to updates for other cities, even if user modifies something in JS

## Bonus tasks

These tasks are optional, but you can implement any or all of them to show more skills.

Order does not matter.

* Unit Test coverage
* Prepare for deployment - provide deployment instructions, config examples, create separate dev & prod environments
* Integrate social login (Facebook, Google, any other OAuth provider of your choice)
* Style the forms (`bootstrap` is already installed in base template, so why don't we use it for forms as well)
* Add more data to weather report (chance of rain, clouds, humidity) and add some styles to output (e.g. output each city as a card, not as a list)
* Dockerize it!
* Rewrite dashboard with some frontend library (Vue, React, Angular)
* Allow to subscribe to new city weather without page reload (AJAX call + API)
* Allow to unsubscribe from some city.
* Add user quota (how much cities he can subscribe to). Also you can make it flexible - e.g. basic plan - 3 cities, premium - 15 cities. *You don't have to implement payments, as it's too long for test task (unless you can integrate some payemnt gateway in 3 hours). So some checkbox in admin panel is acceptable*