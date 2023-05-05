from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(requset):
    return render(requset ,'index.html')

def index(request):
    return HttpResponse('Welcome to page')
