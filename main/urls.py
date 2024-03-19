from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # Path to main html file
]