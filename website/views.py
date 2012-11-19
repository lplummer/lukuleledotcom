ofrom django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render

from website.models import *

def bikes(request):
    return render(request, 'bikes.html')
def index(request):
    return render(request, 'base.html')