from django.db import models

# Модель элементов меню
class Menu(models.Model):
    text = models.CharField(max_length=255)
    parent_menu = models.IntegerField(null=False)
