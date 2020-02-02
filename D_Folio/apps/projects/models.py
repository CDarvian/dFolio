from django.db import models

# Create your models here.

class Project(models.Model):
	project_name = models.CharField('Название', max_length = 60)

	project_description = models.TextField('Описание')
	project_short_description = models.CharField('Краткое описание', max_length = 250)

	project_cover = models.CharField('Ссылка на обложку', max_length = 1200)

	start_date = models.CharField('Дата начала работы', max_length = 10)
	end_date = models.CharField('Дата окончания работы', max_length = 10)

	used_tech = models.TextField('Использованные технологии (через , + пробел)')
	used_tech_link = models.TextField('Ссылки на технологии (через , + пробел)')

	repo_link = models.CharField('Ссылка на исходный код', max_length = 1200)

	view_link = models.CharField('Ссылка на готовый проект', max_length = 1200)

	project_status = models.IntegerField('Статус')

	def __str__(self):
		return self.project_name

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'
