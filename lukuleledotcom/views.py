from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render


def index(requeset):
    return render(request, 'index.html')