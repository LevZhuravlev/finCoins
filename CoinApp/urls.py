from django.urls import path, include
from .views import startApp

urlpatterns = [
    path('', startApp, name='start')
]
