from django.contrib import admin
from main.models import *

# Регистрация моделей для изменения через админку
admin.site.register(Menu)
admin.site.register(MenuBar)