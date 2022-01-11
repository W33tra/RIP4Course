from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('Название книги', max_length=200)
    genre = models.CharField('Жанр книги', max_length=200)
    year = models.CharField('Год написания', max_length=4)

class Chapter(models.Model):
    chapter_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField('Название главы', max_length=500)
    page = models.IntegerField('Страница главы')
