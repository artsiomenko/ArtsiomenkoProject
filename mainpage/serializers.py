from rest_framework import serializers
from mainpage.models import NewsModels, AdModels


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModels
        fields = ('NewsID', 'NewsDate', 'NewsTitle', 'NewsContent', 'NewsContentShort')


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdModels
        fields = ('AdID', 'AdDate', 'AdTitle', 'AdContent', 'AdContentShort')