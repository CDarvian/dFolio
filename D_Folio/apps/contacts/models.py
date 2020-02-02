from django.db import models

# Create your models here.

class Project_request(models.Model):
	sender_name = models.CharField('Имя отправителя', max_length = 60)
	sender_email = models.EmailField('Email отправителя', max_length = 150)

	sender_text = models.TextField('Сообщение отправителя')

	def __str__(self):
		return self.sender_name

	class Meta:
		verbose_name = 'Запрос на проект'
		verbose_name_plural = 'Запросы на проект'

class Project_ask_request(models.Model):
	sender_name = models.CharField('Имя отправителя', max_length = 60)
	sender_email = models.EmailField('Email отправителя', max_length = 150)

	sender_text = models.TextField('Сообщение отправителя')

	def __str__(self):
		return self.sender_name

	class Meta:
		verbose_name = 'Запрос на вопрос по проекту'
		verbose_name_plural = 'Запросы на вопрос по проекту'

class Website_error_request(models.Model):
	sender_name = models.CharField('Имя отправителя', max_length = 60)
	sender_email = models.EmailField('Email отправителя', max_length = 180)

	sender_text = models.TextField('Сообщение отправителя')

	def __str__(self):
		return self.sender_name

	class Meta:
		verbose_name = 'Запрос на ошибку в сайте'
		verbose_name_plural = 'Запросы на ошибку в сайте'

class Other_request(models.Model):
	sender_name = models.CharField('Имя отправителя', max_length = 60)
	sender_email = models.EmailField('Email отправителя', max_length = 180)

	sender_text = models.TextField('Сообщение отправителя')

	def __str__(self):
		return self.sender_name

	class Meta:
		verbose_name = 'Запрос на другое'
		verbose_name_plural = 'Запросы на другое'
