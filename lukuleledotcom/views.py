from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
import urllib

def index(request):
	return render(request, 'index.html')
	
def page(request, active):
	page = str(active)
	return render(request, page+'.html', {page:'active'})
	
def lauren(request):
	return render(request, 'lauren.html')