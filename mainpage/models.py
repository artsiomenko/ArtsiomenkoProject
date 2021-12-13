from django.db import models


class NewsModels(models.Model):
    NewsID = models.AutoField(primary_key=True)
    NewsDate = models.DateTimeField(auto_now_add=True)
    NewsTitle = models.CharField(max_length=100)
    NewsContent = models.CharField(max_length=5000)
    NewsPhoto = models.ImageField(upload_to='images/news/', null=True, blank=True)
    NewsContentShort = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-NewsID']