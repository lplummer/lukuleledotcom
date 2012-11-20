from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
import urllib
from models import *

def index(request):
	return render(request, 'index.html')

def page(request, active):
	args = {str(active):'active'}
	args['entries']=[]
	return render(request, str(active)+'.html', args)
	
def lauren(request):
	return render(request, 'lauren.html')