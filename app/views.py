from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def venky(request):
    return HttpResponse('i love my lucky cham')
