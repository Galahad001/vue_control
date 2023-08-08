from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    content = models.TextField(verbose_name='Описание')
    author = models.CharField(max_length=200, null=True, verbose_name='Автор')
    path_to_photo = models.TextField(verbose_name='Путь к фото', null=True)
    the_year_of_publishing = models.CharField(max_length=20, verbose_name='Дата публикации', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')
    time_update = models.DateField(auto_now=True, verbose_name='Дата изменения поста')
    visibility = models.BooleanField(default=True, verbose_name='Видимость', null=True)
    index = models.IntegerField(unique=True,  verbose_name='id', null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'

# Create your models here.
