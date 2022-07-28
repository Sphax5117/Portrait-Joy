from django.http import HttpResponse, response
from django.shortcuts import render
from httplib2 import Http
from main.models import Creations


def index(request):
    creations = Creations.objects.all()
    return render(request, "index.html", {'creations': creations})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def creations(request):
    return render(request, "creations.html")