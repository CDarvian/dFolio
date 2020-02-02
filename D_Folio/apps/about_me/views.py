from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Work, Education, Tool, Bottom_block

# Create your views here.

def index(request):
	works = Work.objects.all()
	educations = Education.objects.all()
	tools = Tool.objects.all()
	bottom_block = Bottom_block.objects.order_by('-id')[:1]

	return render(request, 'about_me/main.html',
		{
		'works' : works,
		'educations' : educations,
		'tools' : tools,
		'bottom_block' : bottom_block,
		})
