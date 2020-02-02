# Generated by Django 3.0.2 on 2020-01-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bottom_block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=60, verbose_name='Название блока')),
                ('block_description', models.CharField(max_length=500, verbose_name='Описание блока:')),
            ],
            options={
                'verbose_name': 'Нижний блок',
                'verbose_name_plural': 'Нижние блоки',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name', models.CharField(max_length=60, verbose_name='Название')),
                ('edu_place', models.CharField(max_length=80, verbose_name='Место обучения')),
                ('edu_description', models.CharField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образования',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=60, verbose_name='Название инструмента')),
                ('tool_level', models.IntegerField(verbose_name='Уровень владения (1-100)')),
            ],
            options={
                'verbose_name': 'Инструмент',
                'verbose_name_plural': 'Инструменты',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_place', models.CharField(max_length=60, verbose_name='Должность')),
                ('work_company', models.CharField(max_length=60, verbose_name='Компания')),
                ('work_description', models.CharField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
            },
        ),
    ]
