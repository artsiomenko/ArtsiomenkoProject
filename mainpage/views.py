from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from mainpage.models import NewsModels
from mainpage.serializers import NewsSerializer


def index(request):
    news = NewsModels.objects.all()
    return render(request, 'index.html', {'news': news})


def edit(request, id=0):
    news = NewsModels.objects.get(NewsID=id)
    return render(request, 'edit.html', {'news': news})


@csrf_exempt
def newsapi(request,id=0):
    if request.method=='GET':
        news = NewsModels.objects.all()
        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)
    elif request.method=='POST':
        news_data = JSONParser().parse(request)
        news_serializer = NewsSerializer(data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method=='PUT':
        news_data = JSONParser().parse(request)
        news = NewsModels.objects.get(NewsID=news_data['NewsID'])
        news_serializer = NewsSerializer(news, data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse('Update successfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method=='DELETE':
        news = NewsModels.objects.get(NewsID=id)
        news.delete()
        return JsonResponse('Delete successfully', safe=False)