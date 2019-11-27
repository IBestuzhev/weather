from django.views.generic import FormView
from django.views.generic.list import BaseListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.core.management import call_command
from django.core.signing import TimestampSigner, BadSignature
from django.urls import reverse_lazy

from .forms import WeatherSubscribeForm
from .models import WeatherData


class HomeView(LoginRequiredMixin, BaseListView, FormView):
    template_name = 'index.html'
    model = WeatherData
    form_class = WeatherSubscribeForm
    context_object_name = 'weather_data'
    success_url = reverse_lazy('weather-index')

    def get_queryset(self):
        return self.request.user.weatherdata_set.all()

    def form_valid(self, form):
        city = form.cleaned_data['city']
        city_data: WeatherData
        city_data, _created = WeatherData.objects.get_or_create(city=city)
        city_data.subscribed_users.add(self.request.user)
        return super().form_valid(form)


def test_view(request):
    call_command('get_weather')
    return HttpResponse('OK')


def get_user_cities(request, token):
    try:
        signer = TimestampSigner()
        value = signer.unsign(token, max_age=600)
    except BadSignature:
        cities = []
    else:
        cities = list(WeatherData.objects
                      .filter(subscribed_users=value)
                      .values_list('pk', flat=True))
    return JsonResponse({'cities': cities})
