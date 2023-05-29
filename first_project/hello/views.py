from django.shortcuts import render
# se importa HTTPRESPONSE
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hola desde mi primera vista!")

def author(request):
    return HttpResponse("Autor: Evelyn GS.😎")