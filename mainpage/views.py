import requests
from django.http import JsonResponse
from django.shortcuts import render
from geopy.geocoders import Nominatim

from mainpage.models import NewsModels
from mainpage.models import AdModels
from django.utils.encoding import smart_str


def index(request):
    news = NewsModels.objects.all()
    return render(request, 'index.html', {'news': news})


def view_news(request, id=0):
    news = NewsModels.objects.get(NewsID=id)
    return render(request, 'view_news.html', {'news': news})


def ads(request):
    print('alloha')
    ads_data = AdModels.objects.all()
    return render(request, 'ads.html', {'ads': ads_data})


def yandex_weather(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    response = requests.get(
        'https://api.weather.yandex.ru/v2/forecast',
        params={
            'lat': lat,
            'lon': lon,
            'lang': 'ru-RU'
        },
        headers={'X-Yandex-API-Key': '7d65403d-ff87-4c14-a701-aee578d4fe2c'},
    )
    json_response = response.json()
    city = get_city(lat, lon)
    return JsonResponse(
        {
            'temp': json_response.get('fact').get('temp'),
            'city': city
        },
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )


def get_city(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(lat + "," + lon)
    address = location.raw['address']
    city = address.get('city', '')
    return city
