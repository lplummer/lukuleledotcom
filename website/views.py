ofrom django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render

from website.models import *

def index(requeset):
    return render(request, 'index.html')