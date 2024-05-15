from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at Lorem ipsum Home page")
    return render(request , 'website/index.html')


def about(request):
    return HttpResponse("Hello, world. You are at Lorem ipsum About page")

def contact(request):
    return HttpResponse("Hello, world. You are at Lorem ipsum Contact page")