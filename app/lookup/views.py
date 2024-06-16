from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def lookup(request):
    return HttpResponse("Hello, world. You're at the lookup view.")
