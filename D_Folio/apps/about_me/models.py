from django.db import models

# Create your models here.

class Work(models.Model):
	work_place = models.CharField('Должность', max_length = 60)
	work_company = models.CharField('Компания', max_length = 60)
	work_description = models.CharField('Описание', max_length = 250)

	work_period = models.CharField('Период работы', max_length = 17)

	def __str__(self):
		return self.work_company

	class Meta:
		verbose_name = 'Работа'
		verbose_name_plural = 'Работы'

class Education(models.Model):
	edu_name = models.CharField('Название', max_length = 60)
	edu_place = models.CharField('Место обучения', max_length = 80)
	edu_description = models.CharField('Описание', max_length = 250)

	edu_period = models.CharField('Период обучения', max_length = 17)

	def __str__(self):
		return self.edu_name

	class Meta:
		verbose_name = 'Образование'
		verbose_name_plural = 'Образования'

class Tool(models.Model):
	tool_name = models.CharField('Название инструмента', max_length = 60)
	tool_level = models.IntegerField('Уровень владения (1-100)')

	def __str__(self):
		return self.tool_name

	class Meta:
		verbose_name = 'Инструмент'
		verbose_name_plural = 'Инструменты'

class Bottom_block(models.Model):
	block_name = models.CharField('Название блока', max_length = 60)
	block_description = models.CharField('Описание блока:', max_length = 500)

	def __str__(self):
		return self.block_name

	class Meta:
		verbose_name = 'Нижний блок'
		verbose_name_plural = 'Нижние блоки'
