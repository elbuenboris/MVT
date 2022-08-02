from django. http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse('ola desde la segunda clase')
    