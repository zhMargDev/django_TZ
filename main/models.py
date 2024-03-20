from django.db import models


class MenuBar(models.Model): # Это модель которая хранит данные об всех меню
    name = models.CharField(max_length=255)

class Menu(models.Model): # Эта модель хранит данные об элементах
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=255)