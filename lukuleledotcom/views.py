from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')