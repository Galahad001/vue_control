# Generated by Django 3.2 on 2023-08-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_books_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='visibility',
            field=models.BooleanField(default=True, null=True, verbose_name='Видимость'),
        ),
    ]
