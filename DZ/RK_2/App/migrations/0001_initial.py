# Generated by Django 3.2.10 on 2021-12-18 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('genre', models.CharField(max_length=200, verbose_name='Жанр книги')),
                ('year', models.CharField(max_length=4, verbose_name='Год написания')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название главы')),
                ('page', models.IntegerField(verbose_name='Страница главы')),
                ('chapter_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.book')),
            ],
        ),
    ]