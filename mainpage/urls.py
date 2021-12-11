from django.conf.urls import url
from mainpage import views

urlpatterns=[
    url(r'^news$', views.NewsModels),
    url(r'^news/([0-9]+)', views.NewsModels)
]
