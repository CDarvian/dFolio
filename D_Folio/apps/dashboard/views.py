from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	return HttpResponse('I am dashboard!')
