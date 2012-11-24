from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
import urllib
from models import *

def index(request):
	return render(request, 'index.html')

def blog(request):
	args = {'blog':'active', 'entries':[{'title':e.title,'date':e.date,'content':e.content,'author':e.author} for e in BlogPost.objects.all()]}
	return render(request, 'blog.html', args)
	
def page(request, active):
	return render(request, str(active)+'.html', {str(active):'active'})
	
def lauren(request):
	return render(request, 'lauren.html')