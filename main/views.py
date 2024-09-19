from lib2to3.fixes.fix_input import context
import requests
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import serializers
from django.contrib.auth.models import User

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    url = "https://api.waifu.im/search"
    response = requests.get(url)

    if response.status_code == 200:
        waifu_data = response.json()
        print(waifu_data)
        data = {"data": waifu_data.get('images', [])}

        return render(request, "main/index.html", context=data)
    return render(request, "main/index.html", context={"data": []})