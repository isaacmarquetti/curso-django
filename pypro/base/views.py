from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>')

