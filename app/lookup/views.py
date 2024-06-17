from django.http import HttpResponse
from django.shortcuts import render

from .models import Spelling


def index(request):
    return HttpResponse('To look up a word, go to whatgender.is/your-word')


# Create your views here.
def lookup(request, spelling):
    try:
        words = Spelling.objects.get(spelling=spelling).words.all()
    except Spelling.DoesNotExist:
        return HttpResponse(f"We don't know the word {spelling} :(")
    return render(request, 'lookup/lookup.html', {'words': words, 'spelling': spelling.lower()})
