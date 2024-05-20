from django.shortcuts import render

# Create your views here.

def all_django(request):
    return render(request, 'djangoApp/all_django.html')
