from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def startApp(requset):
    return render(requset, 'CoinApp/login.html')