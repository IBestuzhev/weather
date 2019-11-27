from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='weather-index'),
    path('test/', views.test_view),
    path('get-cities/<str:token>/', views.get_user_cities, name='get-user-cities'),
]
