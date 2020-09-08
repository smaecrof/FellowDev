from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Fellow Dev"""
    return render(request, 'fellow_devs/index.html')
