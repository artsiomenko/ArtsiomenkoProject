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


class AdModels(models.Model):
    AdID = models.AutoField(primary_key=True)
    AdDate = models.DateTimeField(auto_now_add=True)
    AdTitle = models.CharField(max_length=100)
    AdContent = models.CharField(max_length=5000)
    AdPhoto = models.ImageField(upload_to='images/news/', null=True, blank=True)
    AdContentShort = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'


class LawsModels(models.Model):
    LawID = models.AutoField(primary_key=True)
    LawDate = models.DateTimeField(auto_now_add=True)
    LawTitle = models.CharField(max_length=100)
    LawFile = models.FileField(upload_to='laws/', null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Нормативные документы'
        verbose_name = 'Нормативный документ'
