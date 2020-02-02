from django.db import models

# Create your models here.

class Main_skill(models.Model):
	skill_name = models.CharField('Название навыка', max_length = 60)
	skill_description = models.CharField('Описание навыка', max_length = 250)

	skill_icon_class = models.CharField('CSS класс иконки навыка', max_length = 60)

	def __str__(self):
		return self.skill_name

	class Meta:
		verbose_name = 'Главный навык'
		verbose_name_plural = 'Главные навыки'

class Laptop_block(models.Model):
	block_name = models.CharField('Название блока', max_length = 60)
	block_description = models.CharField('Описание блока', max_length = 250)

	laptop_image = models.CharField('Ссылка на обложку', max_length = 1200)

	def __str__(self):
		return self.block_name

	class Meta:
		verbose_name = 'Блок с ноутбуком'
		verbose_name_plural = 'Блоки с ноутбуками'