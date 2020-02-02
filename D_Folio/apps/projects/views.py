from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Project

# Create your views here.

def index(request):
	projects_list = Project.objects.all()

	return render(request, 'projects/main.html', 
		{
		'projects' : projects_list,
		})

def detail(request, project_id):
	try:
		p = Project.objects.get(id = project_id)
	except:
		raise Http404('Проект не найден!')

	techs = dict( zip( (p.used_tech).split(', '), (p.used_tech_link).split(', ') ) )

	last_projects = Project.objects.order_by('-id')[:4]

	prj_status = p.project_status

	if prj_status == 1:
		prj_status = 'Рассмотрение'

	elif prj_status == 2:
		prj_status = 'Согласование'

	elif prj_status == 3:
		prj_status = 'Выполнение'

	elif prj_status == 4:
		prj_status = 'Завершение'

	elif prj_status == 5:
		prj_status = 'Завершен'

	elif prj_status == 6:
		prj_status = 'Отправление'

	elif prj_status == 7:
		prj_status = 'Закрыт'
	
	elif prj_status == 8:
		prj_status = 'Завершен'

	return render(request, 'projects/view.html', 
		{
		'prj' : p,
		'tch' : techs,
		'last_prj' : last_projects,
		'p_status' : prj_status,
		})
