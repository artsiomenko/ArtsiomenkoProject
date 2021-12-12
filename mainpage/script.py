import requests

res = requests.get('https://api.weather.yandex.ru/v2/forecast')

print(res)