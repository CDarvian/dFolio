from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Main_skill, Laptop_block
from projects.models import Project

# Create your views here.

def index(request):
	main_skills = Main_skill.objects.order_by('-id')[:3]
	laptop_block = Laptop_block.objects.order_by('-id')[:1]

	last_projects = Project.objects.order_by('-id')[:3]

	return render(request, 'index/main.html', 
		{
		'main_skills' : main_skills,
		'laptop_block' : laptop_block,
		'last_prj' : last_projects,
		})
