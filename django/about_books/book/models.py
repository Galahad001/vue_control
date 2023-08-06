from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

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
