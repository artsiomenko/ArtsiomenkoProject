from rest_framework import serializers
from mainpage.models import NewsModels

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModels
        fields=('NewsID', 'NewsDate', 'NewsTitle', 'NewsContent')