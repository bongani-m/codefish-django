from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!", content-type="text/plain") 

def home(request):
    return render(request, 'home.html')
