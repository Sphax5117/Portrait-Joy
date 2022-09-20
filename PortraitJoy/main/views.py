from django.http import HttpResponse, response
from django.shortcuts import render
from httplib2 import Http
from main.models import Creations


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def tarifs(request):
    return render(request, "tarifs.html")

def services(request):
    return render(request, "services.html")

def creations(request):
    creations = Creations.objects.all()
    return render(request, "creations.html", {'creations': creations})