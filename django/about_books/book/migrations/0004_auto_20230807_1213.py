# Generated by Django 3.2 on 2023-08-07 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='path_to_photo',
            field=models.TextField(null=True, verbose_name='Путь к фото'),
        ),
        migrations.AddField(
            model_name='books',
            name='the_year_of_publishing',
            field=models.CharField(max_length=20, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='books',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='books',
            name='content',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='books',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста'),
        ),
        migrations.AlterField(
            model_name='books',
            name='time_update',
            field=models.DateField(auto_now=True, verbose_name='Дата изменения поста'),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название книги'),
        ),
    ]
